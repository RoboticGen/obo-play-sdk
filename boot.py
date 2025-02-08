from machine import Pin, PWM, SoftI2C, time_pulse_us
import framebuf
#The classes for starting oled display
# register definitions
SET_CONTRAST        = const(0x81)
SET_ENTIRE_ON       = const(0xa4)
SET_NORM_INV        = const(0xa6)
SET_DISP            = const(0xae)
SET_MEM_ADDR        = const(0x20)
SET_COL_ADDR        = const(0x21)
SET_PAGE_ADDR       = const(0x22)
SET_DISP_START_LINE = const(0x40)
SET_SEG_REMAP       = const(0xa0)
SET_MUX_RATIO       = const(0xa8)
SET_COM_OUT_DIR     = const(0xc0)
SET_DISP_OFFSET     = const(0xd3)
SET_COM_PIN_CFG     = const(0xda)
SET_DISP_CLK_DIV    = const(0xd5)
SET_PRECHARGE       = const(0xd9)
SET_VCOM_DESEL      = const(0xdb)
SET_CHARGE_PUMP     = const(0x8d)

# ============================
# SSD1306 Class
# ============================   

class SSD1306:
    def __init__(self, width, height, external_vcc):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = self.height // 8
        # Note the subclass must initialize self.framebuf to a framebuffer.
        # This is necessary because the underlying data buffer is different
        # between I2C and SPI implementations (I2C needs an extra byte).
        self.poweron()
        self.init_display()

    def init_display(self):
        for cmd in (
            SET_DISP | 0x00, # off
            # address setting
            SET_MEM_ADDR, 0x00, # horizontal
            # resolution and layout
            SET_DISP_START_LINE | 0x00,
            SET_SEG_REMAP | 0x01, # column addr 127 mapped to SEG0
            SET_MUX_RATIO, self.height - 1,
            SET_COM_OUT_DIR | 0x08, # scan from COM[N] to COM0
            SET_DISP_OFFSET, 0x00,
            SET_COM_PIN_CFG, 0x02 if self.height == 32 else 0x12,
            # timing and driving scheme
            SET_DISP_CLK_DIV, 0x80,
            SET_PRECHARGE, 0x22 if self.external_vcc else 0xf1,
            SET_VCOM_DESEL, 0x30, # 0.83*Vcc
            # display
            SET_CONTRAST, 0xff, # maximum
            SET_ENTIRE_ON, # output follows RAM contents
            SET_NORM_INV, # not inverted
            # charge pump
            SET_CHARGE_PUMP, 0x10 if self.external_vcc else 0x14,
            SET_DISP | 0x01): # on
            self.write_cmd(cmd)
        self.fill(0)
        self.show()

    def poweroff(self):
        self.write_cmd(SET_DISP | 0x00)

    def contrast(self, contrast):
        self.write_cmd(SET_CONTRAST)
        self.write_cmd(contrast)

    def invert(self, invert):
        self.write_cmd(SET_NORM_INV | (invert & 1))

    def show(self):
        x0 = 0
        x1 = self.width - 1
        if self.width == 64:
            # displays with width of 64 pixels are shifted by 32
            x0 += 32
            x1 += 32
        self.write_cmd(SET_COL_ADDR)
        self.write_cmd(x0)
        self.write_cmd(x1)
        self.write_cmd(SET_PAGE_ADDR)
        self.write_cmd(0)
        self.write_cmd(self.pages - 1)
        self.write_framebuf()

    def fill(self, col):
        self.framebuf.fill(col)

    def pixel(self, x, y, col):
        self.framebuf.pixel(x, y, col)

    def scroll(self, dx, dy):
        self.framebuf.scroll(dx, dy)

    def text(self, string, x, y, col=1):
        self.framebuf.text(string, x, y, col)


class SSD1306_I2C(SSD1306):
    def __init__(self, width, height, i2c, addr=0x3c, external_vcc=False):
        self.i2c = i2c
        self.addr = addr
        self.temp = bytearray(2)
        # Add an extra byte to the data buffer to hold an I2C data/command byte
        # to use hardware-compatible I2C transactions.  A memoryview of the
        # buffer is used to mask this byte from the framebuffer operations
        # (without a major memory hit as memoryview doesn't copy to a separate
        # buffer).
        self.buffer = bytearray(((height // 8) * width) + 1)
        self.buffer[0] = 0x40  # Set first byte of data buffer to Co=0, D/C=1
        self.framebuf = framebuf.FrameBuffer1(memoryview(self.buffer)[1:], width, height)
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        self.temp[0] = 0x80 # Co=1, D/C#=0
        self.temp[1] = cmd
        self.i2c.writeto(self.addr, self.temp)

    def write_framebuf(self):
        # Blast out the frame buffer using a single I2C transaction to support
        # hardware I2C interfaces.
        self.i2c.writeto(self.addr, self.buffer)

    def poweron(self):
        pass
       
oled = {'scl': 22,'sda': 21,'width':128,'height':64}
i2c = SoftI2C(scl=Pin(oled["scl"]), sda=Pin(oled["sda"]))
OLED = SSD1306_I2C(oled["width"], oled["height"], i2c)
       
roboticgen_logo = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x078\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~\xff\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00\x00\x06\x03\x80\x00\x00\x00\x00\x00\x00\x07\xfc\x00\x00\xf0\x00\x00\x0e\x07\x80\x00\x0f\x80\x00\x00\x00\x07\xfe\x00\x00p\x00\x00\x0e\x07\x80\x00?\xe0\x00\x00\x00\x07\xff\x00\x00p\x00\x00\x0e\x03\x00\x00\x7f\xe0\x00\x00\x00\x07\x07\x80\x00`\x00\x00\x0e\x00\x00\x00\xf0`\x00\x00\x00\x07\x03\x83\xf0\x7f\xc0~\x1f\xf3\x87\xe1\xe0\x00|\x07\xc0\x07\x01\xc7\xf8\x7f\xe0\xff\x1f\xf3\x8f\xf9\xc0\x01\xff?\xe0\x07\x01\xcf\xfc\x7f\xf1\xff\x9f\xf3\x9f\xf9\xc0\x01\xef?\xf0\x07\x01\xde\x1exs\xc3\x8e\x03\x9c1\x80\x03\x8e<p\x07\x03\x9c\x0eps\x81\xce\x03\x9c\x01\x80s\x9e88\x07\x8f\x9c\xcew;\x99\xce\x03\xb8\x01\xc0s\x1c88\x07\xff\x1c\xcec3\x99\xce\x03\xb8\x01\xc0s888\x07\xfe\x1c\x0eps\x81\xce\x03\xbc\x01\xe0s\xf088\x07\xfe\x1e\x1cx\xf3\xc3\x87\x03\x9e0\xf0s\xe288\x07\x0e\x0f\xfc?\xf1\xff\x87\xf3\x9f\xf8\x7f\xf1\xff88\x07\x07\x07\xf8?\xe0\xff\x03\xf3\x8f\xf8?\xe0\xff88\x07\x07\x03\xf0\x0f\x80~\x01\xf3\x83\xe0\x1f\xc0|\x180\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
oboplay_logo = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x03\xe0\x00\x03\x80\x00\xff\x80@\x00\x03\x02\x00\x04\x03\xfc\x03 `\x1e\xf0\x00\x80\xe0\xc0\x00\x03\x83\x00\x0c\x04\x03\x02\x0000\x18\x00\x000\xc0\x00\x04\x81\x80\x18\x08\x01\x82\x00\x10`\x0c\x00\x00\x18\xc0\x00\x04\x80\xc00\x10\x00\x82\x00\x10\xc0\x04\x10\x00\x08\xc0\x00\x0c@``0\x00\xc2\x00\x10\x83\x82\x00\x00\x08\xc0\x00\x08@0\xc0 \x80B\x000\x87\xc2\x00\x00\x08\xc0\x00\x18 \x08\x80 \xf0B\x00a\x8f\xe2\x00\x00\x08\xc0\x00\x10 \x00\x00 \xf8B\x03\xc1\x0f\xe2\x01\x80\x18\xc0\x0000\x00\x00 \xe0B\x00a\x8f\xc2\x00\x800\xc0\x00 \x10\x00\x00 \x80B\x000\x87\xc2\x01\x80\xe0\xc0\x00 \x18\x02\x00\x10\x00\xc2\x00\x10\x81\x02\x01\x80\x00\xc0\x00@\x08\x06\x00\x18\x00\x82\x00\x10\xc0\x04\x11\x80\x00\xc0\x00@\x0c\x02\x00\x08\x01\x02\x00\x10`\x0c\x01\x80\x00\xc0\x00\xc0\x04\x06\x00\x06\x06\x02\x0000\x18\x00\x80\x00\xc0\x00\x80\x04\x02\x00\x03\xfc\x02\x03\xe0\x1f\xe0\x01\x80\x00\xff\xf9\x80\x02\x06\x00\x00`\x02\x03\x00\x01\x00\x00\x00\x00\x7f\xf9\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
fb = framebuf.FrameBuffer(roboticgen_logo, 128, 33, framebuf.MONO_HLSB)
OLED.framebuf.blit(fb, 0, 14)
OLED.show()

time.sleep(1)

fb = framebuf.FrameBuffer(oboplay_logo, 128, 24, framebuf.MONO_HLSB)
OLED.fill(0)
OLED.framebuf.blit(fb, 0, 20)
OLED.show()

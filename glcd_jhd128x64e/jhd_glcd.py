import time
import RPi.GPIO as GPIO

# 5x7 size font which have characters with ASCII value 32 to 127 that are displayed in GLCD
look_up = [[0x00, 0x00, 0x00],                    # Space
           [0x00, 0x4f, 0x00],                    # !
           [0x00, 0x07, 0x00, 0x07, 0x00],        # "
           [0x14, 0x7f, 0x14, 0x7f, 0x14, 0x00],  # #
           [0x24, 0x2a, 0x7f, 0x2a, 0x12, 0x00],  # $
           [0x23, 0x13, 0x08, 0x64, 0x62, 0x00],  # %
           [0x36, 0x49, 0x55, 0x22, 0x20, 0x00],  # &
           [0x00, 0x05, 0x03, 0x00],              # '
           [0x00, 0x1c, 0x22, 0x41, 0x00],        # (
           [0x00, 0x41, 0x22, 0x1c, 0x00],        # )
           [0x14, 0x08, 0x3e, 0x08, 0x14, 0x00],  # *
           [0x08, 0x08, 0x3e, 0x08, 0x08, 0x00],  # +
           [0x50, 0x30, 0x00],                    # ,
           [0x08, 0x08, 0x08, 0x08, 0x08, 0x00],  # -
           [0x00, 0x60, 0x60, 0x00],              # .
           [0x20, 0x10, 0x08, 0x04, 0x02, 0x00],  # /
           [0x3e, 0x51, 0x49, 0x45, 0x3e, 0x00],  # 0
           [0x40, 0x42, 0x7f, 0x40, 0x40, 0x00],  # 1
           [0x42, 0x61, 0x51, 0x49, 0x46, 0x00],  # 2
           [0x21, 0x41, 0x45, 0x4b, 0x31, 0x00],  # 3
           [0x18, 0x14, 0x12, 0x7f, 0x10, 0x00],  # 4
           [0x27, 0x45, 0x45, 0x45, 0x39, 0x00],  # 5
           [0x3c, 0x4a, 0x49, 0x49, 0x30, 0x00],  # 6
           [0x01, 0x71, 0x09, 0x05, 0x03, 0x00],  # 7
           [0x36, 0x49, 0x49, 0x49, 0x36, 0x00],  # 8
           [0x06, 0x49, 0x49, 0x29, 0x1e, 0x00],  # 9
           [0x00, 0x36, 0x36, 0x00],              # :
           [0x00, 0x56, 0x36, 0x00],              # ;
           [0x08, 0x14, 0x22, 0x41, 0x00],        # <
           [0x14, 0x14, 0x14, 0x14, 0x14, 0x00],  # =
           [0x00, 0x41, 0x22, 0x14, 0x08, 0x00],  # >
           [0x02, 0x01, 0x51, 0x09, 0x06, 0x00],  # ?
           [0x3e, 0x41, 0x5d, 0x55, 0x1e, 0x00],  # @
           [0x7e, 0x11, 0x11, 0x11, 0x7e, 0x00],  # A
           [0x7f, 0x49, 0x49, 0x49, 0x36, 0x00],  # B
           [0x3e, 0x41, 0x41, 0x41, 0x22, 0x00],  # C
           [0x7f, 0x41, 0x41, 0x22, 0x1c, 0x00],  # D
           [0x7f, 0x49, 0x49, 0x49, 0x41, 0x00],  # E
           [0x7f, 0x09, 0x09, 0x09, 0x01, 0x00],  # F
           [0x3e, 0x41, 0x49, 0x49, 0x7a, 0x00],  # G
           [0x7f, 0x08, 0x08, 0x08, 0x7f, 0x00],  # H
           [0x00, 0x41, 0x7f, 0x41, 0x00],        # I
           [0x20, 0x40, 0x41, 0x3f, 0x01, 0x00],  # J
           [0x7f, 0x08, 0x14, 0x22, 0x41, 0x00],  # K
           [0x7f, 0x40, 0x40, 0x40, 0x40, 0x00],  # L
           [0x7f, 0x02, 0x0c, 0x02, 0x7f, 0x00],  # M
           [0x7f, 0x04, 0x08, 0x10, 0x7f, 0x00],  # N
           [0x3e, 0x41, 0x41, 0x41, 0x3e, 0x00],  # O
           [0x7f, 0x09, 0x09, 0x09, 0x06, 0x00],  # P
           [0x3e, 0x41, 0x51, 0x21, 0x5e, 0x00],  # Q
           [0x7f, 0x09, 0x19, 0x29, 0x46, 0x00],  # R
           [0x26, 0x49, 0x49, 0x49, 0x32, 0x00],  # S
           [0x01, 0x01, 0x7f, 0x01, 0x01, 0x00],  # T
           [0x3f, 0x40, 0x40, 0x40, 0x3f, 0x00],  # U
           [0x1f, 0x20, 0x40, 0x20, 0x1f, 0x00],  # V
           [0x3f, 0x40, 0x38, 0x40, 0x3f, 0x00],  # W
           [0x63, 0x14, 0x08, 0x14, 0x63, 0x00],  # X
           [0x07, 0x08, 0x70, 0x08, 0x07, 0x00],  # Y
           [0x61, 0x51, 0x49, 0x45, 0x43, 0x00],  # Z
           [0x00, 0x7f, 0x41, 0x41, 0x00],        # [
           [0x02, 0x04, 0x08, 0x10, 0x20, 0x00],  # \
           [0x00, 0x41, 0x41, 0x7f, 0x00],        # ]
           [0x04, 0x02, 0x01, 0x02, 0x04, 0x00],  # ^
           [0x40, 0x40, 0x40, 0x40, 0x40, 0x00],  # _
           [0x00, 0x00, 0x03, 0x05, 0x00],        # `
           [0x20, 0x54, 0x54, 0x54, 0x78, 0x00],  # a
           [0x7F, 0x44, 0x44, 0x44, 0x38, 0x00],  # b
           [0x38, 0x44, 0x44, 0x44, 0x44, 0x00],  # c
           [0x38, 0x44, 0x44, 0x44, 0x7f, 0x00],  # d
           [0x38, 0x54, 0x54, 0x54, 0x18, 0x00],  # e
           [0x04, 0x04, 0x7e, 0x05, 0x05, 0x00],  # f
           [0x08, 0x54, 0x54, 0x54, 0x3c, 0x00],  # g
           [0x7f, 0x08, 0x04, 0x04, 0x78, 0x00],  # h
           [0x00, 0x44, 0x7d, 0x40, 0x00],        # i
           [0x20, 0x40, 0x44, 0x3d, 0x00],        # j
           [0x7f, 0x10, 0x28, 0x44, 0x00],        # k
           [0x41, 0x7f, 0x40, 0x00],              # l
           [0x7c, 0x04, 0x7c, 0x04, 0x78, 0x00],  # m
           [0x7c, 0x08, 0x04, 0x04, 0x78, 0x00],  # n
           [0x38, 0x44, 0x44, 0x44, 0x38, 0x00],  # o
           [0x7c, 0x14, 0x14, 0x14, 0x08, 0x00],  # p
           [0x08, 0x14, 0x14, 0x14, 0x7c, 0x00],  # q
           [0x7c, 0x08, 0x04, 0x04, 0x00],        # r
           [0x48, 0x54, 0x54, 0x54, 0x24, 0x00],  # s
           [0x04, 0x04, 0x3f, 0x44, 0x44, 0x00],  # t
           [0x3c, 0x40, 0x40, 0x20, 0x7c, 0x00],  # u
           [0x1c, 0x20, 0x40, 0x20, 0x1c, 0x00],  # v
           [0x3c, 0x40, 0x30, 0x40, 0x3c, 0x00],  # w
           [0x44, 0x28, 0x10, 0x28, 0x44, 0x00],  # x
           [0x0c, 0x50, 0x50, 0x50, 0x3c, 0x00],  # y
           [0x44, 0x64, 0x54, 0x4c, 0x44, 0x00],  # z
           [0x08, 0x36, 0x41, 0x41, 0x00, 0x00],  # {
           [0x00, 0x00, 0x77, 0x00],              # |
           [0x00, 0x41, 0x41, 0x36, 0x08, 0x00],  # }
           [0x08, 0x08, 0x2a, 0x1c, 0x08, 0x00],  # ~
           [0x08, 0x1c, 0x2a, 0x08, 0x08, 0x00]]  # DEL


class KS0108(object):
    """
    class KS0108 is responsible each and every action talking place in this code except the lookup table
    which is called in the main program for execution
    """
    # Timing constants
    E_PULSE = 0.0000001
    E_DELAY = 0.0000005

    def __init__(self, rs, rw, en, d0, d1, d2, d3, d4, d5, d6, d7, chip_set0, chip_set1, reset):
        """
        Description: This function is responsible for pin map, initialize GPIO pins (GPIO.BCM is used) and
        initialize the chip, line and cursor position
        :param rs: Instruction Register Selection if rs=0 and Data Register Selection if rs=1
        :param rw: If rw=0 register Read and if rw=1 register write
        :param en: Enable signal
        :param d0...d7: 8 bit input/output lines
        :param chip_set0: Chip selection for KS0108 IC1
        :param chip_set1: Chip selection for KS0108 IC2
        :param reset: reset signal, Display is OFF if reset=0 and ON if reset=1
        """
        self.chip_set0 = chip_set0
        self.chip_set1 = chip_set1
        self.reset = reset
        self.en = en
        self.rs = rs
        self.rw = rw
        self.d0 = d0
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.d5 = d5
        self.d6 = d6
        self.d7 = d7
        GPIO.setwarnings(False)                        # Disable warnings
        GPIO.setmode(GPIO.BCM)                         # Use BCM GPIO numbers
        GPIO.setup(self.en, GPIO.OUT)
        GPIO.setup(self.rw, GPIO.OUT)
        GPIO.setup(self.rs, GPIO.OUT)
        GPIO.setup(self.d0, GPIO.OUT)
        GPIO.setup(self.d1, GPIO.OUT)
        GPIO.setup(self.d2, GPIO.OUT)
        GPIO.setup(self.d3, GPIO.OUT)
        GPIO.setup(self.d4, GPIO.OUT)
        GPIO.setup(self.d5, GPIO.OUT)
        GPIO.setup(self.d6, GPIO.OUT)
        GPIO.setup(self.d7, GPIO.OUT)
        GPIO.setup(self.chip_set0, GPIO.OUT)
        GPIO.setup(self.chip_set1, GPIO.OUT)
        GPIO.output(self.rs, 0)
        GPIO.output(self.rw, 0)
        GPIO.output(self.en, 0)
        GPIO.output(self.chip_set0, 0)
        GPIO.output(self.chip_set1, 0)
        GPIO.setup(self.reset, GPIO.OUT)
        GPIO.output(self.reset, 0)
        time.sleep(0.002)
        GPIO.output(self.reset, 1)
        time.sleep(0.002)
        self.chip_Num = 0
        self.Line_Num = 0
        self.Cursor_Pos = 0
        self.chipnum = 0

    def use_chipset0(self):
        """
        Description: This function enables Chipset 1(KS0108 IC1) of GLCD.
        :return: None
        """
        GPIO.output(self.chip_set0, 1)       # Turn ON left controller
        GPIO.output(self.chip_set1, 0)       # Turn OFF right controller

    def use_chipset1(self):
        """
        Description: This function enables Chipset 2(KS0108 IC2) of GLCD.
        :return:
        """
        GPIO.output(self.chip_set0, 0)       # Turn OFF left controller
        GPIO.output(self.chip_set1, 1)       # Turn ON right controller

    def clear(self):
        """
        Description: This function clears previously stored data in the memory by writing 0x00 in all memory location
        because there is no command to clear memory in KS0108 IC.
        :return: None
        """
        for c in range(2):
            for y in range(8):
                for i in range(64):
                    self.set_cursor(c, y, i)
                    self.data_write(0x00, 1)

    def start(self):
        """
        Description: Initialization of GLCD, 0x3F command is used to turn on the GLCD.
        0xC0 is start line command
        :return: None
        """
        self.use_chipset0()
        self.data_write(0x3F, 0)
        self.use_chipset1()
        self.data_write(0x3F, 0)
        time.sleep(0.000001)
        self.use_chipset0()
        self.data_write(0xC0, 0)
        self.use_chipset1()
        self.data_write(0xC0, 0)
        self.clear()                        # Clears display and move the cursor to beginning of Chip 0

    def data_write(self, value, mode):
        """
        Description: This function is responsible to send command to the GLCD like Line, Cursor position and to turn ON
        display also to display the data to GLCD.
        :param value: Hex value as commands or from lookup table written on Display based on input given
        :param mode: When RS = 0 Value is written as command to GLCD if RS = 1 written data is displayed on GLCD
        :return:
        """
        self.busy_chk()                      # Check if controller is busy
        GPIO.output(self.rw, 0)
        GPIO.output(self.rs, mode)
        GPIO.output(self.d0, value & 0x01)
        GPIO.output(self.d1, value & 0x02)
        GPIO.output(self.d2, value & 0x04)
        GPIO.output(self.d3, value & 0x08)
        GPIO.output(self.d4, value & 0x10)
        GPIO.output(self.d5, value & 0x20)
        GPIO.output(self.d6, value & 0x40)
        GPIO.output(self.d7, value & 0x80)
        self.toggle()                         # Enable pulse to prevent from loss of data

    def toggle(self):
        """
        Description: Send pulse to enable signal so that the data is not lost during the process.
        :return: None
        """
        time.sleep(self.E_DELAY)
        GPIO.output(self.en, True)
        time.sleep(self.E_PULSE)
        GPIO.output(self.en, False)
        time.sleep(self.E_DELAY)

    def busy_chk(self):
        """
        Description: This functions is used check whether GLCD is busy, waits until the controller is busy.
        d7 pin is set as input to read busy signal and set back as output when busy signal is 0
        :return: None
        """
        GPIO.setup(self.d7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # d7 pin set as input
        GPIO.output(self.rw, 1)                                   # Register read mode
        GPIO.output(self.rs, 0)                                   # Instruction register mode
        self.toggle()                                             # Send pulse to enable signal

        while GPIO.input(self.d7):                                # Wait until busy
            pass
        GPIO.setup(self.d7, GPIO.OUT)                             # d7 set back as output

    def set_cursor(self, chip, line, cursor_pos):
        """
        Description: This function is used to specify when data is to be written on the glcd.
        :param chip: If 0 data will be written on chipset 0, if 1 data will be written on chipset 1
        :param line: Used to specify on when line data is to be written (0 to 7)
        :param cursor_pos: Used to specify on which column data is to be written (0 to 127)
        :return: None
        """
        if chip > 0x01 or cursor_pos >= 128 or line > 0x07:
            raise ValueError("Invalid input")               # Error raised if input is out of boundary
        if ((chip == 0x00) or (chip == 0x01)) and ((line >= 0x00) and (line <= 0x07)) and (
                (cursor_pos >= 0x00) and (cursor_pos < 128)):
            if chip == 0x00:
                self.use_chipset0()                         # Enable chipset 0
            else:
                self.use_chipset1()                         # Enable chipset 1
            self.chip_Num = chip
            self.chipnum = chip
            self.Line_Num = line + 0xB8
            self.Cursor_Pos = cursor_pos + 0x40
            self.data_write(self.Cursor_Pos, 0)             # Cursor position is sent to GLCD as command
            self.data_write(self.Line_Num, 0)               # Line number is sent to GLCD as command

    def go_to_chipset(self, chip):
        """
        Description: Enables chipset 0 or 1 based on the value given by user or value passed in other function.
        :param chip: Chipset 0 is enabled if chip=0, Chipset 1 is enabled if chip=1
        :return: None
        """
        if (chip == 0) or (chip == 1):
            if chip == 0:
                self.use_chipset0()
            else:
                self.use_chipset1()
            self.chip_Num = chip
            self.Cursor_Pos = 0x40
            self.data_write(self.Cursor_Pos, 0)
            self.data_write(self.Line_Num, 0)

    def go_to_line(self, value):
        """
        Description: This function is used to specify on which line the data is to be displayed.
        :param value: Displays data on line 0 to 7 based on user input
        :return: None
        """
        if value <= 0x07:
            self.Line_Num = value + 0xB8
            self.go_to_chipset(self.chipnum)
        else:
            raise ValueError("Value must be between 0 to 7")

    def go_to_nextline(self):
        """
        Description: This function shifts the line position by 1 when it is called in other function
        or called by user
        :return: None
        """
        self.Line_Num += 1
        if self.Line_Num > 0xBF:
            self.Line_Num = 0xB8
        self.go_to_chipset(self.chipnum)

    def print_str(self, data):
        """
        Description: The data is converted to string and sent as characters to print_chr function
        :param data: Data in the form of string/char/int/float
        :return: None
        """
        string = str(data)
        for i in range(len(string)):
            self.print_chr(string[i])

    def print_chr(self, data):
        """
        Description: In this function data received as character and by using the ASCII value of characters the data
        is fetched from lookup table and written in the display, if the data exceeds the line limit it is automatically
        shifted to the next line.
        :param data: Data received as Characters
        :return: none

        Note: ASCII value of char is subtracted by 32 to match with lookup table address
        """
        length = (ord(data) - 32)
        if data == "\n":
            self.go_to_nextline()
        if data != "\n":
            if (self.chip_Num == 0x00) & (self.Cursor_Pos >= 0x80):       # Shift to chipset 1 if Cursor position > 63
                self.go_to_chipset(1)
            for j in range(len(look_up[length])):
                data1 = (look_up[length][j])                              # Fetching data from lookup table
                self.data_write(data1, 1)
                self.Cursor_Pos += 1
                if (self.chip_Num == 0x01) and (self.Cursor_Pos > 0x7F):  # Shift to next line if Cursor position > 127
                    self.go_to_nextline()
                if self.Cursor_Pos >= 0x80:                               # Shift to chipset 1 if Cursor position > 63
                    self.go_to_chipset(1)

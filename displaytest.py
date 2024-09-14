import pyfirmata2

board = pyfirmata2.Arduino('COM3')

LCD_PRINT = 0x01
LCD_CLEAR = 0x02
LCD_SET_CURSOR = 0x03
STRING_SYSEX_COMMAND = 0x27

def sendText(message, message2=None):
    board.send_sysex(LCD_CLEAR, [])
    message_bytes = [ord(char) for char in message]
    board.send_sysex(LCD_SET_CURSOR, [0, 0])
    board.send_sysex(LCD_PRINT, message_bytes)

    if message2 is not None:
        message_bytes2 = [ord(char) for char in message2]
        board.send_sysex(LCD_SET_CURSOR, [0, 1])
        board.send_sysex(LCD_PRINT, message_bytes2)

sendText("solo arriba")

# board.send_sysex(LCD_CLEAR, [])
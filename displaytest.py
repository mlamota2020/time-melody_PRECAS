import pyfirmata2

board = pyfirmata2.Arduino('COM7')

STRING_SYSEX_COMMAND = 0x27

def sendText(message):
    message_bytes = [ord(char) for char in message]
    board.send_sysex(STRING_SYSEX_COMMAND, message_bytes)

while True:
    sendText("habla pe")

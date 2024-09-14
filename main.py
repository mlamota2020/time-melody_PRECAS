import datetime
import time
import pyfirmata
import pygame
import pyaudio

pygame.mixer.init()  # listos mic y bocina
p = pyaudio.PyAudio()

input_stream = p.open( # entrada mic
    format=pyaudio.paInt16,
    channels=1,
    rate=22050,
    input=True,
    frames_per_buffer=1024,
    input_device_index=0
)

output_stream = p.open( # salida mic
    format=pyaudio.paInt16,
    channels=1,
    rate=22050,
    output=True,
    frames_per_buffer=1024
)

print('mic detected\nreading microphone...')


t_h = 17
t_m = 25
t_s = 00
pygame.mixer.music.load("C:\\Users\\inval\\OneDrive\\Documentos\\Audacity\\BEAM - PDF.wav") # Reemplazar

board = pyfirmata.Arduino('COM3') #conexión arduino

LCD_PRINT = 0x01
LCD_CLEAR = 0x02
LCD_SET_CURSOR = 0x03

def sendText(message, message2=None): # crea los textos a ser enviados al lcd
    board.send_sysex(LCD_CLEAR, [])
    message_bytes = [ord(char) for char in message]
    board.send_sysex(LCD_SET_CURSOR, [0, 0])
    board.send_sysex(LCD_PRINT, message_bytes)

    if message2 is not None:
        message_bytes2 = [ord(char) for char in message2]
        board.send_sysex(LCD_SET_CURSOR, [0, 1])
        board.send_sysex(LCD_PRINT, message_bytes2)

print("showing time and date on lcd display!")
while True:

    # agarramos la hora y la fecha
    now = datetime.datetime.now()
    frmttime = now.strftime('%H:%M:%S')
    frmtdate = now.strftime(f"%d/%m/%Y")

    # la mostramos en el lcd
    sendText(f"    {frmttime}    ", f"   {frmtdate}   ")

    # al llegar la hora...
    if (now.hour == t_h and now.minute == t_m and now.second == t_s):
        print('alarm ready!')
        pygame.mixer.music.play() # reproducimos alarma
        
        for x in range(0, 4): # avisamos en lcd
            board.digital[13].write(1)
            sendText("!!!!!!!!!!!!!!!!", "!!!!!!!!!!!!!!!!")
            time.sleep(0.100)

            board.digital[13].write(0)
            board.send_sysex(LCD_CLEAR, [])
            sendText("!!!!!!!!!!!!!!!!", "!!!!!!!!!!!!!!!!")
            time.sleep(0.100)
        print('showing time and date on lcd again...') # continuamos

    #limpieza regular del lcd y el timing
    time.sleep(1)
    board.send_sysex(LCD_CLEAR, [])

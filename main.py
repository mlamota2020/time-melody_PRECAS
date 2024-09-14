import datetime
import time
import pyfirmata
import pygame
import pyaudio

pygame.mixer.init()
p = pyaudio.PyAudio()

input_stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=22050,
    input=True,
    frames_per_buffer=1024,
    input_device_index=0
)

output_stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=22050,
    output=True,
    frames_per_buffer=1024
)

print('detected\nreading and writing microphone...')

t_h = 11
t_m = 32
t_s = 00
pygame.mixer.music.load("C:\\Users\\Robotica1\\Downloads\\03 No soy Eterno.flac") # Reemplazar

board = pyfirmata.Arduino('COM7')

LCD_PRINT = 0x01
LCD_CLEAR = 0x02
LCD_SET_CURSOR = 0x03

while True:
    now = datetime.datetime.now()
    frmttime = now.strftime('%H:%M:%S')
    print(frmttime)

    message = frmttime
    board.send_sysex(LCD_CLEAR, [])
    message_bytes = [ord(char) for char in message]
    board.send_sysex(LCD_SET_CURSOR, [0, 0])
    board.send_sysex(LCD_PRINT, message_bytes)

    if (now.hour == t_h and now.minute == t_m and now.second == t_s):
        print('¡Hora del almuerzo para Bachillerato! (14:58 PM) \n\n Preparando alarma...')
        pygame.mixer.music.play()
        
        for x in range(0, 4):
            board.digital[13].write(1)
            time.sleep(0.100)
            board.digital[13].write(0)
            time.sleep(0.100)


    time.sleep(1)
    board.send_sysex(LCD_CLEAR, [])

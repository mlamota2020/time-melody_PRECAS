import datetime
import time
import pyfirmata2
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

t_h = 19
t_m = 58
t_s = 00
pygame.mixer.music.load("C:\\Users\\inval\\OneDrive\\Documentos\\Audacity\\BEAM - PDF.wav") # Reemplazar

board = pyfirmata2.Arduino('COM3')

while True:
    now = datetime.datetime.now()
    frmttime = now.strftime('%H:%M:%S')
    print(f"It's {frmttime}.")

    if (now.hour == t_h and now.minute == t_m and now.second == t_s):
        print('¡Hora del almuerzo para Bachillerato! (14:58 PM) \n\n Preparando alarma...')
        pygame.mixer.music.play()
        
        for x in range(0, 4):
            board.digital[13].write(1)
            print('1')
            time.sleep(0.100)
            board.digital[13].write(0)
            print('0')
            time.sleep(0.100)


    time.sleep(1)
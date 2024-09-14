import pyaudio

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

print('detected\nreading and writing micrphone...')



try:
    while True:
        data = input_stream.read(1024)
        output_stream.write(data)

except KeyboardInterrupt:
    print('stop')
    input_stream.stop_stream()
    input_stream.close()
    output_stream.stop_stream()
    output_stream.close()
    p.terminate()


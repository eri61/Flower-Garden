import pyaudio

CHUNK=1024
RATE=44100
p=pyaudio.PyAudio()

stream=p.open(  format = pyaudio.paInt16,
                channels = 1,
                rate = RATE,
                frames_per_buffer = CHUNK,
                input = True,
                output = True) # inputとoutputを同時にTrueにする

while stream.is_active():
    input = stream.read(CHUNK)
    output = stream.write(input)
#    print(input[0:10])
    
stream.stop_stream()
stream.close()
p.terminate()

print("Stop Streaming")

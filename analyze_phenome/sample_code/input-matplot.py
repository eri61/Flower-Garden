import pyaudio
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024
RATE = 16000
pa = pyaudio.PyAudio()

stream = pa.open(   format = pyaudio.paFloat32,
                    channels = 1,
                    rate = RATE,
                    frames_per_buffer = CHUNK,
                    input = True,
                    output = True)

while stream.is_active():
    input = stream.read(CHUNK)
    input = np.fromstring(input, np.float32)

    wave_x = range(0, CHUNK)
    wave_y = input

    plt.clf()
    plt.plot(wave_x, wave_y)
    plt.axis([0, CHUNK, -0.5, 0.5])
    plt.xlabel("time [sample]")
    plt.ylabel("amplitude")
    plt.pause(.01)
    output = stream.write(input)

stream.stop_stream()
stream.close()
pa.terminate()

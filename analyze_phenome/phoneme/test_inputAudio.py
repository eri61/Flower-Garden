import pyaudio
import wave
import sys
import numpy as np

CHUNK = 1024

p = pyaudio.PyAudio()

stream = p.open(for

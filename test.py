import struct
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import noisereduce as nr
import scipy.io.wavfile as wavfile
r, d = wavfile.read('test_1.wav')

reduced = nr.reduce_noise(y=d, sr=r)

# print(reduced)

# spf = wave.open("test_1.wav", "r")

# # Extract Raw Audio from Wav File
# signal = spf.readframes(10000000)

signal = np.frombuffer(reduced, dtype=np.int16)

Time = np.linspace(0, len(signal) / r, num=len(signal))
# s = struct.pack('h'*len(signal), *signal)

# signal = struct.pack('h'*len(signal), *signal)

# # If Stereo
# if (spf.getnchannels() == 2):
#     print("Just mono files")
#     sys.exit(0)

plt.figure(1, figsize=(100,8))
plt.title("Signal Wave...")
plt.plot(Time, signal)
plt.ylim(bottom=0)
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import convolve
from numpy.fft import fft, ifft

# ---------------------------
# Load audio and impulse response
# ---------------------------
# Replace with your files
audio_rate, audio = wavfile.read("audio.wav")
ir_rate, ir = wavfile.read("impulse_response.wav")

# If stereo, convert to mono
if audio.ndim > 1:
    audio = np.mean(audio, axis=1)
if ir.ndim > 1:
    ir = np.mean(ir, axis=1)

# Normalize
audio = audio.astype(float) / np.max(np.abs(audio))
ir = ir.astype(float) / np.max(np.abs(ir))

# ---------------------------
# Linear Convolution
# ---------------------------
linear_conv = convolve(audio, ir, mode="full")

# ---------------------------
# Circular Convolution (via FFT)
# ---------------------------
N = len(audio) + len(ir) - 1  # match linear length
A = fft(audio, N)
B = fft(ir, N)
circular_conv = np.real(ifft(A * B))

# ---------------------------
# Visualization
# ---------------------------
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(audio, color="blue")
plt.title("Original Audio Signal 3EK3 16 Saniya Mamti")
plt.xlabel("Samples")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2)
plt.plot(linear_conv, color="green")
plt.title("Linear Convolution (Audio * Impulse Response)")
plt.xlabel("Samples")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 3)
plt.plot(circular_conv, color="red")
plt.title("Circular Convolution (FFT-based)")
plt.xlabel("Samples")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

# ---------------------------
# Save output (optional)
# ---------------------------
linear_conv_norm = (linear_conv / np.max(np.abs(linear_conv)) * 32767).astype(np.int16)
circular_conv_norm = (circular_conv / np.max(np.abs(circular_conv)) * 32767).astype(np.int16)

wavfile.write("linear_convolution.wav", audio_rate, linear_conv_norm)
wavfile.write("circular_convolution.wav", audio_rate, circular_conv_norm)
import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500
t = np.linspace(0, 2, 2 * fs, endpoint=False)

# Signals
sine = np.sin(2 * np.pi * 5 * t)   # 5 Hz sine
cosine = np.cos(2 * np.pi * 10 * t)  # 10 Hz cosine
product = sine * cosine

# Plot
plt.figure()
plt.plot(t, product, label="Sine × Cosine")
plt.title("Multiplication of 5 Hz Sine and 10 Hz Cosine - Ek_3_Saniya_Mamti_16")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
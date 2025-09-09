import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

# Original and shifted signals
sine = np.sin(2 * np.pi * 5 * t)
shifted = np.sin(2 * np.pi * 5 * (t - 0.1))  # shift by 0.1s

# Plot
plt.figure()
plt.plot(t, sine, label="Original")
plt.plot(t, shifted, label="Shifted by 0.1s", linestyle="--")
plt.title("Time Shift of 5 Hz Sine Wave - Ek_3_Saniya_Mamti_16")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
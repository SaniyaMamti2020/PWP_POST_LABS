import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

# Original and scaled signals
sine = np.sin(2 * np.pi * 10 * t)
scaled = 3 * sine  # scale by factor of 3

# Plot
plt.figure()
plt.plot(t, sine, label="Original")
plt.plot(t, scaled, label="Scaled ×3", linestyle="--")
plt.title("Amplitude Scaling of 10 Hz Sine Wave - Ek_3_Saniya_Mamti_16")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

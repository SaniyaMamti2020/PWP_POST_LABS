import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)

# Signals
sine1 = np.sin(2 * np.pi * 5 * t)   # 5 Hz sine
sine2 = np.sin(2 * np.pi * 10 * t)  # 10 Hz sine
combined = sine1 + sine2

# Plot
plt.figure()
plt.plot(t, combined, label="5 Hz + 10 Hz")
plt.title("Addition of 5 Hz and 10 Hz Sine Waves - Ek_3_Saniya_Mamti_16")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
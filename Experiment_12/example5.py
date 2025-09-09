import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

# Original and reversed signals
sine = np.sin(2 * np.pi * 5 * t)
reversed_signal = sine[::-1]  # reverse array

# Plot
plt.figure()
plt.plot(t, sine, label="Original")
plt.plot(t, reversed_signal, label="Reversed", linestyle="--")
plt.title("Time Reversal of 5 Hz Sine Wave - Ek_3_Saniya_Mamti_16")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
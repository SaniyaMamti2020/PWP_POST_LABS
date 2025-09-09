import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image
img = Image.open("MU.jpg")  # replace with your image path
img_array = np.array(img)

# Extract channels
R = img_array[:, :, 0]
G = img_array[:, :, 1]
B = img_array[:, :, 2]

# Plot channels
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.imshow(R, cmap="Reds")
plt.title('Red Channel 3EK3 16 Saniya Mamti')
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(G, cmap="Greens")
plt.title('Green Channel 3EK3 16 Saniya Mamti')
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(B, cmap="Blues")
plt.title('Blue Channel 3EK3 16 Saniya Mamti')
plt.axis("off")

plt.tight_layout()
plt.show()
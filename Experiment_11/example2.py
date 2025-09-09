import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

# Load image
img = Image.open("MU.jpg")  # replace with your image path

# Add padding (50 pixels all sides, black color)
padded_img = ImageOps.expand(img, border=50, fill='black')

# Show result
plt.imshow(padded_img)
plt.title('Padded Image with Black Spaces 3EK3 16 Saniya Mamti')
plt.axis("off")
plt.show()
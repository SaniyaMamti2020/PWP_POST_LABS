import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image
img = Image.open("MU.jpg")  # replace with your image path
img_array = np.array(img)

# Image details
dimensions = img.size  # (width, height)
shape = img_array.shape
min_blue = img_array[:, :, 2].min()  # channel B = index 2

print("Dimensions (Width x Height):", dimensions)
print("Shape:", shape)
print("Min pixel value in Blue channel:", min_blue)

# Show image
plt.imshow(img)
plt.title('Original RGB Image 3EK3 16 Saniya Mamti')
plt.axis("off")
plt.show()
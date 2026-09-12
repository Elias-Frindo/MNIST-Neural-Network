from PIL import Image
import numpy as np

# Load image in grayscale
Rimg = Image.open('digit.png').resize((28, 28))

array_2d = np.array(Rimg)
print(array_2d.shape)

array_1d = array_2d.reshape(-1)
print(array_1d.shape)

Mimg = array_1d / 255
print(Mimg)
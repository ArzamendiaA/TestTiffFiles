import tifffile as tiff
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

volume = tiff.imread('Sequence3.tif')
print(volume.shape)
print(volume.dtype)
print(type(volume)) # Numpy array

print(volume[0,:,:])
plt.imshow(volume[0,:,:])
plt.show()

fig, ax = plt.subplots(1, 3, figsize=(20, 5))

for i in range(3):
    ax[i].imshow(volume[i], cmap='gray')
    ax[i].set_title(f'Slide {i}')
    ax[i].axis('off')

plt.tight_layout()
plt.show()
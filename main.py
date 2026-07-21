import tifffile as tiff
import matplotlib.pyplot as plt

volume = tiff.imread('Sequence3.tif')
print(volume.shape)
print(volume.dtype)
print(type(volume)) # Numpy array

fig, ax = plt.subplots(1, 3, figsize=(20, 5))

for i in range(3):
    ax[i].imshow(volume[i], cmap='gray')
    ax[i].set_title(f'Slide {i}')
    ax[i].axis('off')

plt.tight_layout()
plt.show()
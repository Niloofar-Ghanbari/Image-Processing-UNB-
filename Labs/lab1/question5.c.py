from PIL import Image
from PIL import ImageOps
import matplotlib.pyplot as plt

# Open and show the RGB image
Arch_img = Image.open('Arch.jpg')

flip_img = Arch_img.transpose(Image.FLIP_TOP_BOTTOM)
flop_img = Arch_img.transpose(Image.FLIP_LEFT_RIGHT)
rotate_img = Arch_img.transpose(Image.ROTATE_270)
invert_img = ImageOps.invert(Arch_img)

fig, ax = plt.subplots(nrows=2, ncols=2, sharey='all')

ax[0, 0].imshow(flip_img)
ax[0, 0].axis('off')
ax[0, 0].title.set_text('Flip Image')

ax[0, 1].imshow(flop_img)
ax[0, 1].axis('off')
ax[0, 1].title.set_text('Flop Image')

ax[1, 0].imshow(invert_img)
ax[1, 0].axis('off')
ax[1, 0].title.set_text('Invert Image')

ax[1, 1].imshow(rotate_img)
ax[1, 1].axis('off')
ax[1, 1].title.set_text('Rotate Image')


plt.show()



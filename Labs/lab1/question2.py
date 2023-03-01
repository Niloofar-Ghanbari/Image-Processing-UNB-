from PIL import Image

# read a RGB Image
RGB_img = Image.open('Arch.jpg')

# convert to a grey level image
Gray_img = RGB_img.convert('L')

# save as a PNG file
Gray_img.save("final_img.png")

# Resize the grey level image
img_resize = Gray_img.resize((Gray_img.width // 2, Gray_img.height // 2))
img_resize.show()








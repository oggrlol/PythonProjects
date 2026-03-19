from PIL import Image, ImageFilter, ImageEnhance

with Image.open("original.jpg") as original:
    original = Image.open("original.jpg")

tamano = original.size
formato = original.format
tipo = original.mode

print('tamaño:', tamano,"\nformato:", formato,"\ntipo:", tipo)

original_gray = original.convert('L')
original_gray.save('gray.jpg')
original_gray.show()

original_blur = original.filter(ImageFilter.BLUR)
original_blur.save('blured.jpg')
original_blur.show()

original_rotated = original.transpose(Image.ROTATE_180)
original_rotated.save('up.jpg')
original_rotated.show()

original_mirror = original.transpose(Image.FLIP_LEFT_RIGHT)
original_mirror.save('mirror.jpg')
original_mirror.show()

original_contrast = ImageEnhance.Contrast(original)
original_contrast = original_contrast.enhance(1.5)
original_contrast.save('contr.jpg')
original_contrast.show()

original.show()
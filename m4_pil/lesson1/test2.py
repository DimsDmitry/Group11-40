from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open('photo.jpg') as pic_original:
    pic_original.show()

    # pic_gray = pic_original.convert('L')
    # pic_gray.save('coala1.jpg')
    # pic_gray.show()
    #
    # pic_up = pic_gray.transpose(Image.ROTATE_90)
    # pic_up.save('coala2.jpg')
    # pic_up.show()

    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save('blured.jpg')
    pic_blured.show()

    # зеркальное отображение
    pic_mir = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    # save
    # show

    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance(1.5)
    pic_contrast.save('cont.jpg')
    pic_contrast.show()

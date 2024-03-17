from PIL import *

from PIL import Image

with Image.open('photo.jpg') as pic_original:
    print('Размер:', pic_original.size)
    print('Формат:', pic_original.format)
    print('Тип:', pic_original.mode)
    pic_original.show()

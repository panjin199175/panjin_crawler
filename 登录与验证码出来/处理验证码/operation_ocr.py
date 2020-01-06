# encding:utf-8

'''
@author: Hollow
@file: operation_ocr.py
@time: 2019-11-12 11:14

'''

#OCR处理验证码

#把彩色图像转化成灰色
from PIL import Image
im = Image.open('captcha.jpg')
gray = im.convert('L')
gray.show()
gray.save("captcha_gray.jpg")

#二值化处理，加深验证码颜色
threshold = 150
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = gray.point(table, '1')
out.show()
out.save("captcha_thresholded.jpg")

import pytesseract
th = Image.open('captcha_thresholded.jpg')
print(pytesseract.image_to_string(th))
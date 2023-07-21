import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('qr_code.png')


for code in decode(img):
    print(code.data.decode("utf-8"))




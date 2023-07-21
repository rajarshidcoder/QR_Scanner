import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread('qr_code.png')

cam = cv2.VideoCapture(0)

while True:
    _, img = cam.read()
    if decode(img):
        for code in decode(img):
            print(code.data.decode("utf-8"))

    img = cv2.flip(img,1)
    cv2.imshow("Screan", img)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()




import cv2
import numpy as np
from pyzbar.pyzbar import decode


cam = cv2.VideoCapture(0)

while True:
    _, img = cam.read()
    if decode(img):
        for code in decode(img):
            print(code.data.decode("utf-8"))
            points = np.array([code.polygon],np.int32)
            points.reshape((-1,1,2))
            cv2.polylines(img,[points],True,(255,0,255),2)

    img = cv2.flip(img,1)
    cv2.imshow("Screan", img)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()




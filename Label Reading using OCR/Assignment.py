import cv2
import pytesseract

#pytesseract.pytesseract.
tesseract_cmd = r'/usr/local/Cellar/tesseract/'

def recText(img):
    text = pytesseract.pytesseract.image_to_string(img)
    return text

cam = cv2.VideoCapture(0)

while True:
    _,img = cam.read()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    text = "Normal"

    cv2.imshow("Image",img)
    key = cv2.waitKey(1)
    if key == (27):
        info = recText(img)
        print("Conversion:\n",info)
        break


cam.release()
cv2.destroyAllWindows()

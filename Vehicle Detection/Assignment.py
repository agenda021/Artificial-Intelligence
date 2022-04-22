import cv2
import imutils
cascade='cars.xml'

code=cv2.CascadeClassifier(cascade)
cam=cv2.VideoCapture(1)
cam1=cv2.VideoCapture(0)
while True:
    _,img=cam.read()
    img=imutils.resize(img,width=300)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    car=code.detectMultiScale(gray,1.1,1)
    for (x,y,w,h) in car:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("img",img)
    b=(str(len(car)))
    a=int(b)
    detected=a
    n=detected
    print("--------------------------------------")
    print(" North: %d"%(n))
    if n>=2:
        print("North more traffic")
    else:
        print("no traffic")
    if cv2.waitKey(20)==27:
        break
    _, img1 = cam1.read()
    img1 = imutils.resize(img1, width=300)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    car1 = code.detectMultiScale(gray1, 1.1, 1)
    for (x, y, w, h) in car1:
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("img", img1)
    b1 = (str(len(car1)))
    a1 = int(b1)
    detected1 = a1
    n1 = detected1
    print("--------------------------------------")
    print(" South: %d" % (n1))
    if n1 >= 2:
        print("South more traffic")
    else:
        print("no traffic")
    if cv2.waitKey(20) == 27:
        break
cam.release()
cv2.destroyAllWindows()

import cv2

alg = "haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture(0)

txt = "No Person Detected"
while True:
    _,img = cam.read()
    txt = "No Person Detected"
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        faceOnly = grayImg[y:y+h,x:x+w]
        txt = "Person Detected"
    cv2.putText(img,txt,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,255),2)
    cv2.imshow("Face Detection", img)
    key = cv2.waitKey(10)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()

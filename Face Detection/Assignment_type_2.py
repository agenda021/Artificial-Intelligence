import cv2
import os
dataset = "dataset"
name = "khnjn"

path = os.path.join(dataset,name)
if not os.path.isdir(path):
    os.mkdir(path)

(width,height) = (130,100)
alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)
cam = cv2.VideoCapture(0)

count = 0
while count < 51:
    text="No Person Detected"
    _,img = cam.read()
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),2)
        faceOnly = grayImg[y:y+h,x:x+w]
        resizeImg = cv2.resize(faceOnly,(width,height))
        cv2.imwrite("%s/%s.jpg" %(path,count),resizeImg)
        count+=1
        text =  "Person is Detected"
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.imshow("FaceDetection",img)
    key = cv2.waitKey(10) 
    if key == 49:
        break
print("Image Captured succssfully")
cam.release()
cv2.destroyAllWindows()

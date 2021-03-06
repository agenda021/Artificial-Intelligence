import cv2, numpy, os, imutils, urllib.request
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'
print('training...')
url = 'http://192.168.144.226:8080/shot.jpg'
(images, labels, names, id) = ([],[],{},0)

for(subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = id
            images.append(cv2.imread(path,0))
            labels.append(int(label))
        id +=1
(images, labels) = [numpy.array(lis) for lis in [images, labels]]
(width,height) = (130,100)
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)

cnt = 0

face_cascade = cv2.CascadeClassifier(haar_file)

while True:
    imgPath = urllib.request.urlopen(url)
    imgNp = numpy.array(bytearray(imgPath.read()), dtype=numpy.uint8)
    im = cv2.imdecode(imgNp, -1)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im, (x,y),(x+w, y+h), (255,255,0),2)
        face = gray[y:y+h,x:x+w]
        face_resize = cv2.resize(face, (width, height))

        prediction = model.predict(face_resize)
        cv2.rectangle(im, (x,y), (x+w, y+h), (0,255,0))
        if prediction[1] < 800:
            cv2.putText(im,'%s-%.0f' %(names[prediction[0]],prediction[1]), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0,255,0))
            #cv2.FONT_HERSHEY_PLAIN
            print (names[prediction[0]])
            cnt = 0
        else:
            cnt+=1
            cv2.putText(im,'Unknown', (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,2,(255,0,0))
            print("Unknown Person")
            cv2.imwrite("unKnown.jpg", im)
    cv2.imshow('faceRecognition', im)
    key = cv2.waitKey(10)
    if key == 27:
        break
cv2.destroyAllWindows()

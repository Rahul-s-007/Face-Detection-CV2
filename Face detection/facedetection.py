#--Credentials-----------------------------------------------------------------------------

## Author: Rahul V Sumbly
## Copyright: Copyright 2020, Face Detection-CV2
## Credits: Rahul V Sumbly
## License: ~None~
## Version: {mayor}.{minor}.{rel}
## Maintainer: Rahul V Sumbly
## Email: -NA-
## Status: COMPLETED

#-------------------------------------------------------------------------------------------

import cv2

def func(a):
    cap=cv2.VideoCapture(a)

    while True:
        check,output=cap.read()
        faceCascade = cv2.CascadeClassifier('C:\\Users\\RAHUL\\Desktop\\Face detection\\haarcascade_frontalface_default.xml')
        faces=faceCascade.detectMultiScale(output,1.3,5)
        for (x,y,w,h) in faces:
            output = cv2.rectangle(output,(x,y),(x+w,y+h),(255,0,0),2)
            output = cv2.resize(output, (360,240))
            cv2.imshow('face recogonition',output)
        k=cv2.waitKey(1)
        if k==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
func('C:\\Users\\RAHUL\\Desktop\\Face detection\\face_dance.avi')

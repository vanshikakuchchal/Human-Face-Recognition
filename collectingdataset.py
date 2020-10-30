import cv2
profileface = "haarcascade_profileface.xml"
frontalface = "haarcascade_frontalface_default.xml"

profilefacecascade = cv2.CascadeClassifier(profileface)
frontalfacecascade = cv2.CascadeClassifier(frontalface)

video_capture = cv2.VideoCapture(0)
face_id = 3
count=0
while True:
        ret, frame = video_capture.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = frontalfacecascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20),
        flags=cv2.CASCADE_SCALE_IMAGE
        )
        if len(faces) == 0:
            faces = profilefacecascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(20, 20),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
        if len(faces) == 0:
            faces = profilefacecascade.detectMultiScale(
            cv2.flip(gray ,1),
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20),
            flags=cv2.CASCADE_SCALE_IMAGE
            )
            frame = cv2.flip(frame,1)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
                count=count+1
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                cv2.imwrite("Dataset/User."+str(face_id)+'.'+str(count)+".jpg",cv2.flip(roi_gray,1))
            frame = cv2.flip(frame,1)
        else:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
                count=count+1
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                cv2.imwrite("Dataset/User."+str(face_id)+'.'+str(count) +".jpg",roi_gray)
        cv2.imshow('Video', frame)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        if count >=200:
            break
video_capture.release()
cv2.destroyAllWindows()
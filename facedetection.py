import cv2
profileface = "haarcascade_profileface.xml"
frontalface = "haarcascade_frontalface_default.xml"

profilefacecascade = cv2.CascadeClassifier(profileface)
frontalfacecascade = cv2.CascadeClassifier(frontalface)

video_capture = cv2.VideoCapture(0)

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
                gray,blob:file:///bdd7fc1b-7bb0-414a-a1f2-1283ddfc9574
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
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
            frame = cv2.flip(frame,1)
        else:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
    
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
video_capture.release()
cv2.destroyAllWindows()
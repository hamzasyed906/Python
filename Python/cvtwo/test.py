import cv2

face = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
smile = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

camon = cv2.VideoCapture(0)
print("Camera On")
print("Smile = Happy")
print("No Smile = Calm")

while True:
    ret, frame = camon.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 5)

    mood = "Calm"

    for (x, y, w, h) in faces:
        face_gray = gray[y:y+h, x:x+w]

        smiles = smile.detectMultiScale(face_gray, 1.8, 20)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        if len(smiles) > 0:
            mood = "Happy"

            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(
                    frame,
                    (x + sx, y + sy),
                    (x + sx + sw, y + sy + sh),
                    (0, 255, 0),
                    2
                )
                break 

    cv2.putText(
        frame,
        mood,
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Smile Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camon.release()
cv2.destroyAllWindows()

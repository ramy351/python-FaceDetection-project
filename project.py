import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

print("Choose the display mode:")
print("1. Full Screen")
print("2. Small Window")

while True:
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1' or choice == '2':
        break
    else:
        print("Invalid input: Please enter either 1 or 2")

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        print('Error: Frame not captured')
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if choice == '1':

        cv2.namedWindow('Face Detection', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Face Detection', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    elif choice == '2':

        cv2.namedWindow('Face Detection')

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

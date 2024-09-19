import cv2
plate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
cap = cv2.VideoCapture('Automatic Number Plate Recognition (ANPR) _ Vehicle Number Plate Recognition (1).mp4')
while True:
    ret, frame = cap.read()

    if not ret:
        break  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in plates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        plate_region = frame[y:y + h, x:x + w]
    cv2.imshow('Number Plate Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.WaitKey()
cv2.destroyAllWindows()

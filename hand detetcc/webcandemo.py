import cv2

def detect_face(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
    detected_face = classifier.detectMultiScale(gray_img, minSize=(50, 50))

    if len(detected_face) > 0:
        for (x, y, width, height) in detected_face:
            cv2.rectangle(img, (x, y), (x + height, y + width), (0, 255, 255), 4)

    return img


cap = cv2.VideoCapture(0)

while (True):

    ret, frame = cap.read()
    frame = detect_face(frame)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()













import cv2

org_img = cv2.imread('images/face-2.jpg')
gray_img = cv2.cvtColor(org_img, cv2.COLOR_RGB2GRAY)

classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
detected_face = classifier.detectMultiScale(gray_img, minSize=(50, 50))

if len(detected_face) > 0:
   for (x, y, width, height) in detected_face:
       cv2.rectangle(org_img, (x, y), (x + height, y + width), (0, 255,255), 4)

cv2.imshow('Face', org_img)
cv2.waitKey(0)
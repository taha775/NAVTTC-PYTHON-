import cv2

org_img = cv2.imread('images/face-1.jpg')
gray_img = cv2.cvtColor(org_img, cv2.COLOR_RGB2GRAY)

classifier = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
detected_eyes = classifier.detectMultiScale(gray_img, scaleFactor=1.3, minSize=(20, 20), maxSize=(50, 50), minNeighbors = 3)

if len(detected_eyes) > 0:
   for (x, y, width, height) in detected_eyes:
       cv2.rectangle(org_img, (x, y), (x + height, y + width), (0, 255,255), 3)

cv2.imshow('Eyes', org_img)
cv2.waitKey(0)
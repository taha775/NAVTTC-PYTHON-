import cv2
import numpy as np

# Reading and displaying image
# img = cv2.imread('images/clock.jpg')
# cv2.imshow('Clock image', img)
# cv2.waitKey(0)


# Reading and displaying image
# img = cv2.imread('images/clock.jpg')
# cv2.imshow('Clock image', img)
# cv2.waitKey(0)


# Displaying size of image
# img = cv2.imread('images/clock.jpg')
# print(img.shape)

# Getting R, G, B Channels
# img = cv2.imread('images/rgb.jpg')
# b = img[:,:,0]
# g = img[:,:,1]
# r = img[:,:,2]
# cv2.imshow('Color Image', img)
# cv2.imshow('Blue Channel', b)
# cv2.imshow('Green Channel', g)
# cv2.imshow('Red Channel', r)
# cv2.waitKey(0)


# Image representation
# img = cv2.imread('images/deer-1.jpg')
# print(img[0,0,:])


# Region of Interest (ROI)
# img = cv2.imread('images/deer-1.jpg')
# roi_image = img[200:400, 100:320, :]
# cv2.imshow('Original Image', img)
# cv2.imshow('ROI Image', roi_image)
# cv2.waitKey(0)


# Resizing image
# img = cv2.imread('images/deer-1.jpg')
# resized_image = cv2.resize(img, (200,200))
# resized_image = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5, interpolation = cv2.INTER_NEAREST)
# cv2.imshow('Original Image', img)
# cv2.imshow('Resized Image', resized_image)
# cv2.waitKey(0)




# Rotating an image
# img = cv2.imread('images/clock.jpg')
#
# h, w, ch = img.shape
#
# center = (w//2, h//2)
#
# rot_matrix = cv2.getRotationMatrix2D(center,45, 0.5)
# rot_img = cv2.warpAffine(img, rot_matrix, (w, h))
#
# cv2.imshow('Original Image', img)
# cv2.imshow('Rotated Image', rot_img)
# cv2.waitKey(0)





# Canny edge detection and image writing
# img = cv2.imread('images/man-1.jpg')
# img = cv2.resize(img, (0,0), fx=0.7, fy=0.7)
#
# # Canny (image, threshold1, threshold2)
# edge_img = cv2.Canny(img, 200,230)
#
# cv2.imshow('Original Image', img)
# cv2.imshow('Edge Image', edge_img)
# cv2.waitKey(0)


# Sobel detection methods
# img = cv2.imread('images/coins-1.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.GaussianBlur(img, (3,3), 0)


# sobelx = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
# sobely = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
# sobelxy = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)


# cv2.imshow('Original Image', img)
# cv2.imshow('Sobel-X Image', sobelx)
# cv2.waitKey(0)



#cv2.flip()
# Empty images
# np.zeros((500,500), dtype=np.unit)

import cv2

# Load the pre-trained Haar cascade files for face and smile detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read the webcam frame
    ret, frame = cap.read()
    
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # For each detected face, detect smiles
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=15)

        # Draw rectangles around the detected faces and smiles
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

    # Display the resulting frame
    cv2.imshow('Smile Detection', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()

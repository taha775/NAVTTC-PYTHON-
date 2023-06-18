
import mediapipe as mp
import cv2

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils

handdetector = mpHands.Hands()
camera = cv2.VideoCapture(0)  # captures the video

while True:
    success, image = camera.read()  # check  boioloean  value
    rgbimage = cv2.cvtColor(image,cv2.COLOR_BAYER_RG2BGR)  # we have to convert color b/c mediapipe use rgb but in cv bgr

    # PROCESSING
    result = handdetector.process(rgbimage)  # come lands marks in resulkt variable
    if result.multi_hand_landmarks:  # if there is an objetc
        for hand in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(image, hand)

    cv2.imshow("webcame feed", image)
    key = cv2.waitKey(1)
    if key == 27:
        break

camera.realease()
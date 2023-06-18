import cv2
import mediapipe as mp
import numpy as np

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils

handDetector = mpHands.Hands(max_num_hands=6)

camera = cv2.VideoCapture(0)

while True:

    success, image = camera.read()
    image = cv2.flip(image, 1)

    h, w, ch = image.shape

    foregroundImage = np.zeros((h, w, ch))

    rgbImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    result = handDetector.process(rgbImage)

    handcount = 0

    if result.multi_hand_landmarks:

        handcount = len(result.multi_hand_landmarks)
        cv2.putText(image, "HANDS = " + str(handcount), (20,40), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,255), 3)

        hnd = 0
        p1 = None
        p2 = None
        for hand in result.multi_hand_landmarks:

            hnd += 1



            for id, lm in enumerate(hand.landmark):


                x, y = int(lm.x * w), int(lm.y * h)

                if id == 10:
                    if hnd==1:
                        p1 = (x,y)
                    elif hnd==2:
                        p2 = (x,y)

                    cv2.circle(image, (x, y), 10, (0, 255, 255), -1, cv2.LINE_AA)
                    cv2.circle(foregroundImage, (x, y), 10, (0, 255, 255), -1, cv2.LINE_AA)


            if p1 is not None and p2 is not None:
                cv2.line(image, p1, p2, (0,255,0), 5, cv2.LINE_AA)
                cv2.line(foregroundImage, p1, p2, (0, 255, 0), 5, cv2.LINE_AA)

            print(p1, p2)
            mpDraw.draw_landmarks(image, hand, mpHands.HAND_CONNECTIONS)
            mpDraw.draw_landmarks(foregroundImage, hand, mpHands.HAND_CONNECTIONS)


    cv2.imshow('Webcam Feed', image)
    cv2.imshow('Foreground Image', foregroundImage)
    key = cv2.waitKey(1)
    if key == 27:
        break

camera.release()




# import cv2
# import mediapipe as mp
# import numpy as np

# mpHands = mp.solutions.hands
# mpDraw = mp.solutions.drawing_utils

# handDetector = mpHands.Hands(static_image_mode = True, max_num_hands=6)

# camera = cv2.VideoCapture(0)  #if use camera use 0 and if use to video then pot vidoe file

# while True:

#     success, image = camera.read()
#     image = cv2.flip(image, 1)  # mirror image

#     h, w, ch = image.shape

#     foregroundImage = np.zeros((h, w, ch))

#     rgbImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)   # we have to convert

#     result = handDetector.process(rgbImage)  # usinng hand detector instead of rreceiving an image

#     handcount = 0

#     if result.multi_hand_landmarks: # multi world landmarks ,mult hand mar ks and multi handness thrree para meters are there in that para eter

#         handcount = len(result.multi_hand_landmarks)
#         cv2.putText(image, "HANDS = " + str(handcount), (20,40), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,255), 3)

#         hnd = 0
#         p1 = None
#         p2 = None
#         for hand in result.multi_hand_landmarks:

#             hnd += 1



#             for id, lm in enumerate(hand.landmark):


#                 x, y = int(lm.x * w), int(lm.y * h)

#             #     if id == 0:
#             #         if hnd==1:
#             #             p1 = (x,y)
#             #         elif hnd==2:
#             #             p2 = (x,y)


#             #         cv2.circle(image, (x, y), 10, (0, 255, 255), -1, cv2.LINE_AA)
#             #         cv2.circle(foregroundImage, (x, y), 10, (0, 255, 255), -1, cv2.LINE_AA)

#             # if p1 is not None and p2 is not None:
#             #     cv2.line(image, p1, p2, (0,255,0), 5, cv2.LINE_AA)
#             #     cv2.line(foregroundImage, p1, p2, (0, 255, 0), 5, cv2.LINE_AA)


                

#                 if id == 4:
#                     if hnd==1:
#                         p1 = (x,y)
#                     elif hnd==2:
#                         p2 = (x,y)

#                     cv2.circle(image, (x, y), 10, (0, 255, 255), -1, cv2.LINE_AA)
#                     cv2.circle(foregroundImage, (x, y), 10, (0, 255, 255), -1, cv2.LINE_AA)


           
#                     cv2.line(image, p1, p2, (0,255,0), 5, cv2.LINE_AA)
#                 cv2.line(foregroundImage, p1, p2, (0, 255, 0), 5, cv2.LINE_AA)


#                 mpDraw.draw_landmarks(image, hand, mpHands.HAND_CONNECTIONS)
#                 mpDraw.draw_landmarks(foregroundImage, hand, mpHands.HAND_CONNECTIONS)

#                 if id == 8:
#                     if hnd==1:
#                         p1 = (x,y)
#                     elif hnd==2:
#                         p2 = (x,y)


#                     cv2.circle(image, (x, y), 10, (0, 255, 255), -1, cv2.LINE_AA)
#                     cv2.circle(foregroundImage, (x, y), 10, (0, 255, 255), -1, cv2.LINE_AA)


#             if p1 is not None and p2 is not None:
#                 cv2.line(image, p1, p2, (0,255,0), 5, cv2.LINE_AA)
#                 cv2.line(foregroundImage, p1, p2, (0, 255, 0), 5, cv2.LINE_AA)

            #     if id == 12:
            #         if hnd==1:
            #             p1 = (x,y)
            #         elif hnd==2:
            #             p2 = (x,y)

            #         cv2.circle(image, (x, y), 10, (0, 255, 255), -1, cv2.LINE_AA)
            #         cv2.circle(foregroundImage, (x, y), 10, (0, 255, 255), -1, cv2.LINE_AA)


            # if p1 is not None and p2 is not None:
            #     cv2.line(image, p1, p2, (0,255,0), 5, cv2.LINE_AA)
            #     cv2.line(foregroundImage, p1, p2, (0, 255, 0), 5, cv2.LINE_AA)

            #     if id == 16:
            #         if hnd==1:
            #             p1 = (x,y)
            #         elif hnd==2:
            #             p2 = (x,y)

            #         cv2.circle(image, (x, y), 10, (0, 255, 255), -1, cv2.LINE_AA)
            #         cv2.circle(foregroundImage, (x, y), 10, (0, 255, 255), -1, cv2.LINE_AA)


            # if p1 is not None and p2 is not None:
            #     cv2.line(image, p1, p2, (0,255,0), 5, cv2.LINE_AA)
            #     cv2.line(foregroundImage, p1, p2, (0, 255, 0), 5, cv2.LINE_AA)


            #     if id == 20:
            #         if hnd==1:
            #             p1 = (x,y)
            #         elif hnd==2:
            #             p2 = (x,y)
            #     # if id ==6:
            #     #     if hnd ==1:
            #     #         p2 =(x,y)

            #         cv2.circle(image, (x, y), 10, (0, 255, 255), -1, cv2.LINE_AA)
            #         cv2.circle(foregroundImage, (x, y), 10, (0, 255, 255), -1, cv2.LINE_AA)


            # if p1 is not None and p2 is not None:
            #     cv2.line(image, p1, p2, (0,255,0), 5, cv2.LINE_AA)
            #     cv2.line(foregroundImage, p1, p2, (0, 255, 0), 5, cv2.LINE_AA)

#             print(p1, p2)
#             mpDraw.draw_landmarks(image, hand, mpHands.HAND_CONNECTIONS)
#             mpDraw.draw_landmarks(foregroundImage, hand, mpHands.HAND_CONNECTIONS)


#     cv2.imshow('Webcam Feed', image)
#     cv2.imshow('Foreground Image', foregroundImage)
#     key = cv2.waitKey(1)
#     if key == 27:
#         break

# camera.release()


# practice of same  that


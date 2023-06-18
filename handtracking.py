# import cv2 as cv
# import mediapipe as mp
# import numpy as np 


# mpHands  =mp.solutions.hands
# mpDraw =mp.solutions.drawing_utils

# handdetector =mpHands.Hands()
# camera =cv.VideoCapture(0)  # captures the video


# while True:
#     success, image =camera.read()   #check  boioloean  value
#     image = cv.flip(image,1)      #if you disbale that the camera use mirror image
    
#     h,w,ch = image.shape

    
#     rgbimage= cv.cvtColor(image,cv.COLOR_BGR2RGB)  #we have to convert color b/c mediapipe use rgb but in cv bgr 

#     foregroundImage = np.zeros((h,w,ch))

#     handcount  = 0
#     # PROCESSING 
#     result = handdetector.process(rgbimage)   #come lands marks in resulkt variable
#     if result.multi_hand_landmarks: 
#         handcount =len(result.multi_hand_landmarks)
#         cv.putText(image,"HANDS = "+ str(handcount),(20,40),cv.FONT_HERSHEY_PLAIN,2,(0,255,0),3)
    
    
#          # if there is an objetc 
#         for hand in result.multi_hand_landmarks:
#             mpDraw.draw_landmarks(image,hand,mpHands.HAND_CONNECTIONS)
#             mpDraw.draw_landmarks(foregroundImage,hand,mpHands.HAND_CONNECTIONS)
    
#     # img =np.vstack((image,foregroundImage))
    
    
    
    
#     cv.imshow("webcame feed",image)
#     cv.imshow("foreground image",foregroundImage)
#     key =cv.waitKey(1)
#     if key  == 27 :
#         break
    
        
# camera.realease()



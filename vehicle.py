import cv2
import numpy as np

# web camera starting by this line
cap = cv2.VideoCapture('video.mp4')


#initialize Substractor
algo=cv2.bgsegm.createBackgroundSubstractorMOG()


while True:
    ret, frame1 = cap.read()
    grey= cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    blur=cv2.GAussianBlur(grey,(3,3),5)
    #applying on each frame
    img_sub = algo.apply(blur)
    dilat = cv2.dilate()

    cv2.imshow('Video Original', frame1)

    if cv2.waitKey(1) == 13:
        break

cv2.destroyAllWindows()
cap.release()

import numpy as np
import cv2
cap = cv2.VideoCapture('CAM1.mp4')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(noiseSigma = 10)
fgbg2 = cv2.createBackgroundSubtractorMOG2(varThreshold = 200)
fgbg3 = cv2.createBackgroundSubtractorKNN(dist2Threshold = 800)
while(1):
    ret, frame = cap.read()
    # fgmask = fgbg.apply(frame)
    # fgmask2 = fgbg2.apply(frame)
    fgmask3 = fgbg3.apply(frame)
    
    # cv2.imshow('frame',fgmask)

    # cv2.imshow('frame',fgmask2)
    cv2.imshow('frame',fgmask3)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
# fgbg = cv2.bgsegm.createBackgroundSubtractorGMG(decisionThreshold = 0.3)
# while(1):
#     ret, frame = cap.read()
#     fgmask = fgbg.apply(frame)
#     fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
#     cv2.imshow('frame',fgmask)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#       break
cap.release()
cv2.destroyAllWindows()
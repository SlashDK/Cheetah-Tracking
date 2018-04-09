import numpy as np
import cv2
cap = cv2.VideoCapture('CAM1.mp4')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(noiseSigma = 10)
fgbg2 = cv2.createBackgroundSubtractorMOG2(varThreshold = 200)
fgbg3 = cv2.createBackgroundSubtractorKNN(dist2Threshold = 800,detectShadows = False)
kernel = np.ones((5,5),np.uint8)
kernel2 = np.ones((2,2),np.uint8)

while(1):

    ret, frame = cap.read()
    if (ret==False):
      break
    frameorig = frame
    # frame = fgbg.apply(frame)
    # frame = fgbg2.apply(frame)

    # frame = cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)
    # frame =  cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    frame = fgbg3.apply(frame)
    # frame = cv2.GaussianBlur(frame,(5,5),0)
 
    frame = cv2.erode(frame,kernel2,iterations = 1)
    frame = cv2.blur(frame,(10,10))

    frame2 = cv2.dilate(frame,kernel,iterations = 1)
    

    ret, mask = cv2.threshold(frame2, 10, 255, cv2.THRESH_BINARY)
    
    frame2 = cv2.bitwise_and(frameorig,frameorig,mask = mask)
    cv2.imshow('frame',frame2)
    # break
    # break
    # print(np.unique(mask[1]))

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# print(np.unique(mask))


# print(cv2.bitwise_and(np.ndarray([0,1,2]),np.ndarray([1,1,2])))
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
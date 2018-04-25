import numpy as np
import cv2
import os

filelist = []
fileoutputlist = []
for root, directories, filenames in os.walk('D:\Projects\Cheetah Tracking\Data'):
    for filename in filenames:
        fn = (os.path.join(root, filename))
        if(fn[-1] == '4'):
            filelist.append(fn)

#         loc = root.find("Data")
#         newpath = root[:loc] + "Data2" + root[loc + 4:]

#         # print(newpath)
#         if not os.path.exists(newpath):
#             os.makedirs(newpath)
# a = input("asd")
# print(filelist)
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg2 = cv2.createBackgroundSubtractorMOG2(varThreshold=100)
fgbg3 = cv2.createBackgroundSubtractorKNN(
    dist2Threshold=500, detectShadows=False)
kernel = np.ones((5, 5), np.uint8)
kernel2 = np.ones((2, 2), np.uint8)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
for i in filelist:
    cap = cv2.VideoCapture(i)
    loc = i.find("Data")
    outputDirectory = i[:loc] + "Data2" + i[loc + 4:]
    out = cv2.VideoWriter(outputDirectory, fourcc, 90.0, (1920, 1080))
    # out = cv2.VideoWriter("output.mp4", fourcc, 90.0, (1920, 1080))
    print(outputDirectory)
    while(1):

        ret, frame = cap.read()
        if (ret == False):
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

        frame2 = cv2.bitwise_and(frameorig, frameorig, mask=mask)
        # cv2.imshow('frame',frame2)
        out.write(frame2)


        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

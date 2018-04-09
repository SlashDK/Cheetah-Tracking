import numpy as np
import cv2

file_path = "CAM1.mp4"

cap = cv2.VideoCapture(file_path)
first_iter = True
result = None
while(1):
    ret, frame = cap.read()
    if frame is None:
        break

    if first_iter:
        avg = np.float32(frame)
        first_iter = False

    cv2.accumulateWeighted(frame, avg, 0.005)
    result = cv2.convertScaleAbs(avg)
print(type(result))
print(type(frame))
cap = cv2.VideoCapture(file_path)

# while(1):
ret, frame = cap.read()
# fgmask = fgbg.apply(frame)
# fgmask2 = fgbg2.apply(frame)
# fgmask3 = fgbg3.apply(frame)

# cv2.imshow('frame',fgmask)

# cv2.imshow('frame',fgmask2)
# print(type(fram))
try:
    r = result - frame
except:
	pass
# cv2.imshow('frame',frame)
    
    # k = cv2.waitKey(30) & 0xff
    # if k == 27:
    #     break
cv2.imshow("result", r)
cv2.imwrite("averaged_frame.jpg", result)
print(r)
cv2.waitKey(0)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
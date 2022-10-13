import cv2 
import os
import math
import numpy as np

def setLabel(img, pts, label) :
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x,y)
    pt2 = (x + w, y + h)
    cv2.rectangle(img, pt1, pt2, (0,255,0), 2)
    cv2.putText(img, label, (pt1[0], pt1[1]-3), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))



path = r'C:\Users\goback\Downloads\lpr\라벨링\exp28\one_line'
img_name = '20220929-100843_331소6569.jpg'

img_path = os.path.join(path,img_name)
img_array = np.fromfile(img_path, np.uint8)
src = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src,cv2.COLOR_RGB2GRAY)
ret, thr = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cont in contours:
    approx = cv2.approxPolyDP(cont, cv2.arcLength(cont, True) * 0.02, True)
    vtc = len(approx)

    if vtc == 3 :
        setLabel(src, cont, '3')
    elif vtc == 4 :
        setLabel(src, cont, '4')
    elif vtc == 5 :
        setLabel(src, cont, '5')
    else : 
        area = cv2.contourArea(cont)
        _, radius = cv2.minEnclosingCircle(cont)
        try :
            ratio = radius * radius * math.pi / area
            if int(ratio) == 1:
                setLabel(src, cont, '0')
        except Exception as e : print(e)
cv2.imshow("src", src)
cv2.waitKey(0)

cv2.destroyAllWindows()
import cv2, os 
import pytesseract
import numpy as np 

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'
lpr = '153호2115'
letter = '가나다라마거너더러머버서어저고노도로모보소오조구누두루무부수우주아바사자배하허호'
lpr_exam = list(lpr)

path = r'C:\Users\goback\Downloads\lpr\라벨링\exp29\one_line'
img_name = '20220930-122457_52나0581.jpg'

img_path = os.path.join(path,img_name)
img_array = np.fromfile(img_path, np.uint8)
src = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(src, (3,3),0)
# canny = cv2.Canny(blur, 100, 200)
thresh = cv2.threshold(src,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
invert = 255 - opening


text = pytesseract.pytesseract.image_to_string(thresh, lang='kor', config='--psm 6')
print(text)

cv2.imshow('test',thresh)
cv2.waitKey(0)

cv2.destroyAllWindows()


# print(len(lpr_exam))
# if len(lpr_exam) == 8 :
#     if 0<= int(lpr_exam[0]) <=9 and 0<= int(lpr_exam[1]) <=9 and 0<= int(lpr_exam[2]) <=9 and lpr_exam[3] in letter and 0<= int(lpr_exam[4]) <=9 and 0<= int(lpr_exam[5]) <=9 and 0<= int(lpr_exam[6]) <=9 and 0<= int(lpr_exam[7]) <=9:
#         print('True')
# elif len(lpr_exam) == 7 :
#     if 0<= int(lpr_exam[0]) <=9 and 0<= int(lpr_exam[1]) <=9 and lpr_exam[2] in letter and 0<= int(lpr_exam[3]) <=9 and 0<= int(lpr_exam[4]) <=9 and 0<= int(lpr_exam[5]) <=9 and 0<= int(lpr_exam[6]) <=9 :
#         print('True')

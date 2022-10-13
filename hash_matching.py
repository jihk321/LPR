import cv2, os
import numpy as np
import glob

# 영상 읽기 및 표시
path = r'C:\Users\goback\Downloads\lpr\라벨링\exp28\one_line'
img_name = '20220929-100843_331소6569.jpg'

img_path = os.path.join(path,img_name)
img_array = np.fromfile(img_path, np.uint8)
src = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

cv2.imshow('query', src)

# 비교할 영상들이 있는 경로 ---①
search_dir = r'C:\Users\goback\Downloads\lpr\라벨링\exp28\one_line'

# 이미지를 16x16 크기의 평균 해쉬로 변환 ---②
def img2hash(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (16, 16))
    avg = gray.mean()
    bi = 1 * (gray > avg)
    return bi

# 해밍거리 측정 함수 ---③
def hamming_distance(a, b):
    a = a.reshape(1,-1)
    b = b.reshape(1,-1)
    # 같은 자리의 값이 서로 다른 것들의 합
    distance = (a !=b).sum()
    return distance

# 권총 영상의 해쉬 구하기 ---④
query_hash = img2hash(src)

# 이미지 데이타 셋 디렉토리의 모든 영상 파일 경로 ---⑤
img_path = glob.glob(search_dir+'/**/*.jpg')
for path in img_path:
    # 데이타 셋 영상 한개 읽어서 표시 ---⑥
    imgs_array = np.fromfile(path, np.uint8)
    img = cv2.imdecode(imgs_array, cv2.IMREAD_COLOR)
    cv2.imshow('searching...', img)
    cv2.waitKey(5)
    # 데이타 셋 영상 한개의 해시  ---⑦
    a_hash = img2hash(img)
    # 해밍 거리 산출 ---⑧
    dst = hamming_distance(query_hash, a_hash)
    if dst/256 < 0.25: # 해밍거리 25% 이내만 출력 ---⑨
        print(path, dst/256)
        cv2.imshow(path, img)
cv2.destroyWindow('searching...')
cv2.waitKey(0)
cv2.destroyAllWindows()
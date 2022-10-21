import numpy as np
import torch 
import torch.nn as nn
import torch.nn.functional as F
import os, glob, cv2

path = r'C:\Users\goback\Downloads\lpr\라벨링\exp32\one_line'
file_path = os.path.join(path,'*.jpg')
files = glob.glob(file_path)
trash_file = glob.glob(r'C:\Users\goback\Downloads\lpr\라벨링\exp32\one_line\trash\*.jpg')

x_list,y_list = [],[]

for jpg in files :
    img_array = np.fromfile(jpg,np.uint8)
    src = cv2.imdecode(img_array,cv2.IMREAD_COLOR)

    h, w, c = src.shape
    jpg_size = [h,w]
    x_list.append(jpg_size)
    y_list.append([1])
for trash in trash_file :
    img_array = np.fromfile(trash,np.uint8)
    src = cv2.imdecode(img_array,cv2.IMREAD_COLOR)

    h, w, c = src.shape
    trash_size = [h,w]
    x_list.append(trash_size)
    y_list.append([0])

w = torch.zeros((2,1), requires_grad = True)
b = torch.zeros(1, requires_grad = True)

x_train = torch.FloatTensor(x_list)
y_train = torch.FloatTensor(y_list)

print(x_train.shape, y_train.shape)

model = nn.Linear(2,1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

nb_epochs = 2000
for epoch in range(nb_epochs+1):

    # H(x) 계산
    prediction = model(x_train)

    # cost 계산
    cost = F.mse_loss(prediction, y_train) # <== 파이토치에서 제공하는 평균 제곱 오차 함수

    # cost로 H(x) 개선하는 부분
    # gradient를 0으로 초기화
    optimizer.zero_grad()
    # 비용 함수를 미분하여 gradient 계산
    cost.backward() # backward 연산
    # W와 b를 업데이트
    optimizer.step()

    if epoch % 100 == 0:
    # 100번마다 로그 출력
      print('Epoch {:4d}/{} Cost: {:.6f}'.format(
          epoch, nb_epochs, cost.item()
      ))
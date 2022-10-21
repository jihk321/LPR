import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

excel = pd.read_excel('lpr.xlsx', engine='openpyxl', sheet_name= 0, header= 2)

# print(excel['촬영시간'])

three = excel.loc[excel['촬영시간'] == '오후 3시'].to_dict()
five = excel.loc[excel['촬영시간'] == '오후 5시'].values
six = excel.loc[excel['촬영시간'] == '오후 6시'].values
eig = excel.loc[excel['촬영시간'] == '오전 8시'].values


# three_s, five_s, six_s, eig_s = {},{},{},{}
# for i in range(len(three)) :
#     three_s[three[i,8] + '_' + three[i,2]] = three[i,14]
# for i in range(len(five)) :
#     five_s[five[i,8] + '_' + five[i,2]] = five[i,14]
# for i in range(len(six)) :
#     six_s[six[i,8] + '_' + six[i,2]] = six[i,14]
# for i in range(len(eig)) :
#     eig_s[eig[i,8] + '_' + eig[i,2]] = eig[i,14]

# print(three_s,'\n', five_s,'\n', six_s,'\n', eig_s)


print(excel['신규 차량'])

new_car = excel['신규 차량'].to_list()
pre_car = excel['이전 촬영 차량']
plt.hist(new_car, bins=20)
plt.show()
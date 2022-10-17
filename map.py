import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

excel = pd.read_excel('lpr.xlsx', engine='openpyxl', sheet_name= 0, header= 2)

# print(excel['촬영시간'])

three = excel.loc[excel['촬영시간'] == '오후 3시']['차량 수'].to_list()
five = excel.loc[excel['촬영시간'] == '오후 5시']['차량 수'].to_list()
six = excel.loc[excel['촬영시간'] == '오후 6시']['차량 수'].to_list()
eig = excel.loc[excel['촬영시간'] == '오전 8시']['차량 수'].to_list()

total = {'오전 8시' : eig, '오후 3시' : three, '오후 5시' : five, '오후 6시' : six}
# avg = gg.mean()
# avg = avg.to_dict()

plt.bar(len(eig), eig)
plt.bar(len(eig), three)
plt.bar(len(eig), five)
plt.bar(len(eig), six)
plt.show()



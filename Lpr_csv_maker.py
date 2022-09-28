import os 
import csv
from datetime import datetime


file_path = r'C:\Users\goback\Downloads\lpr\라벨링\0906\one_line'
file_list = os.listdir(file_path)
cnt=0

date_flag=datetime.today().strftime("%Y%m%d")
f = open(file_path + '\\' + str(date_flag)+"_LPR.csv", "w", encoding='utf-8-sig')
f.write('번호,날짜,생성파일명,수정파일명,검증\n')

for i in file_list :
    file_name = i
    # 이미지 판별 
    if(file_name[-3:]=='jpg'): 
        cnt=cnt+1
        print(file_name)

        date_text = file_name[0:16]
        f.write(str(cnt) +','+date_text + ','+file_name[16:-4]+ ','+','+'\n')

f.close()












        
        

    






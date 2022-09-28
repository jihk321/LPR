from operator import sub
import os
import pandas as pd

main_dir = '라벨링'
sub_dir = []
now_path = os.getcwd()

def listdirs(main_dir) :
    for i in os.scandir(main_dir) :
        if i.is_dir(): 
            listdirs(i)
            if 'one_line' in i.path or 'two_lines' in i.path:
                if 'trash' not in i.path : sub_dir.append(os.path.join(now_path,i.path))
listdirs(main_dir) #main_dir 하위 폴더 리스트 
print(sub_dir)

f = open(now_path + '\\' + '데이터필터링.csv', "w", encoding='utf-8-sig')
f.write('파일경로,날짜,파일명\n')

for file in sub_dir :
    file_list = os.listdir(file)
    for i in file_list :
        if i.endswith('.jpg') : f.write(file + ',' + i[0:16] + ',' + i[16:-4]+ '\n')
f.close()

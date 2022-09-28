from genericpath import isfile
import os
import shutil
import pandas as pd

now_path = os.getcwd()
file_path = now_path + '//trash'
file_list = os.listdir()
file_name = [file for file in file_list if file.endswith('.csv')]
files = pd.read_csv(file_name[0], header=0, sep=',')
m_cnt, e_cnt, n_cnt = 0,0,0 # 삭제한 파일 갯수, 수정한 파일 갯수, 넘버링

move_file = pd.DataFrame(files[files['수정파일명'].isnull()])
if not os.path.isdir(file_path): os.mkdir(file_path)
for idx, row in move_file.iterrows():

    move_name = str(row['날짜']) + str(row['생성파일명']) + '.jpg'

    try :
        shutil.move(now_path +'\\'+ move_name, file_path +'\\'+ move_name)
        m_cnt = m_cnt + 1
    except :
        remove_name = str(row['날짜'])  + '0' + str(row['생성파일명']) + '.jpg'
        if os.path.isfile(now_path + '\\' + remove_name) :
            shutil.move(now_path +'\\'+ remove_name, file_path +'\\'+ remove_name)
    
edit_file = pd.DataFrame(files[files['검증'].values == 0])

for idx, row in edit_file.iterrows():
    day = str(row['날짜'])
    origin_name = day + row['생성파일명'] + '.jpg'

    if os.path.isfile(now_path + '\\' + origin_name) :
        e_cnt = e_cnt + 1
        try : 
            
            rename = day + row['수정파일명'] + '.jpg'
            os.rename(origin_name,rename)
            n_cnt = 0
        except :
            rename = day + str(row['수정파일명']) + '_0' + str(n_cnt) + '.jpg'
            os.rename(origin_name,rename)

            n_cnt = n_cnt + 1 
    else : 
        origin_name = day +'0'+ str(row['수정파일명']) + '.jpg'
        if os.path.isfile(now_path + '//' + origin_name) :
            e_cnt = e_cnt + 1

            rename = day + '0' + str(row['수정파일명']) + '.jpg'
            os.rename(origin_name,rename)
        
print(f'{e_cnt}개 수정 {m_cnt}개 삭제 ')
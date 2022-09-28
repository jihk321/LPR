from genericpath import isfile
import os
import shutil
import pandas as pd

now_path = r'C:\Users\goback\Downloads\lpr\라벨링\exp23\one_line'
# now_path = r'C:\Users\goback\Downloads\lpr\라벨링\exp22\two_lines'
file_path = now_path + '\\trash'
file_list = os.listdir(now_path)
file_name = [file for file in file_list if file.endswith('.csv')]
file_jpg = [file for file in file_list if file.endswith('.jpg')]

files = pd.read_csv(now_path + '\\' +file_name[0], header=0, sep=',')
m_cnt, e_cnt, n_cnt = 0,0,0 # 삭제한 파일 갯수, 수정한 파일 갯수, 넘버링

move_file = pd.DataFrame(files[files['정답'].isnull()])
if not os.path.isdir(file_path): os.mkdir(file_path)
for idx, row in move_file.iterrows():

    move_name = str(row['날짜']) + str(row['흥']) + '.jpg'

    try :
        shutil.move(now_path +'\\'+ move_name, file_path +'\\'+ move_name)
        m_cnt = m_cnt + 1
    except :
        remove_name = str(row['날짜'])  + '0' + str(row['흥']) + '.jpg'
        if os.path.isfile(now_path + '\\' + remove_name) :
            shutil.move(now_path +'\\'+ remove_name, file_path +'\\'+ remove_name)
            m_cnt = m_cnt + 1
    
edit_file = pd.DataFrame(files[files['검증'].values == 0])

for idx, row in edit_file.iterrows():
    day = str(row['날짜'])
    print(idx)
    # print(len(file_jpg))
    # origin_name = file_jpg[idx]
    rename = day + str(row['정답']) + '.jpg'

    e_cnt = e_cnt + 1
    # try :  os.rename(now_path+'\\'+origin_name,now_path+'\\'+rename)
    # except :
    #     while not os.path.isfile(now_path + '\\' + rename) :
    #         n_cnt = n_cnt + 1 
    #         rename = day = row['정답'] + '_' + str(n_cnt) + '.jpg'
    #         print(rename)
    #         os.rename(now_path+'\\'+origin_name,now_path+'\\'+rename)
        
    # finally : n_cnt = 0

    # if os.path.isfile(now_path + '\\' + origin_name) :
    #     e_cnt = e_cnt + 1
    #     try : 
            
    #         rename = day + row['정답'] + '.jpg'
    #         os.rename(now_path+'\\'+origin_name,now_path+'\\'+rename)
    #         n_cnt = 0
    #     except :
    #         n_cnt = n_cnt + 1 
    #         rename = day + row['정답'] + '_01.jpg'
    #         print(day,row['정답'],n_cnt)
    #         os.rename(now_path+'\\'+origin_name,now_path+'\\'+rename)
    # else : 
    #     origin_name = day + row['흥'] + '0'+'.jpg'
    #     if os.path.isfile(now_path + '//' + origin_name) :
    #         e_cnt = e_cnt + 1

    #         rename = day + str(row['정답']) +'01'+ '.jpg'
    #         os.rename(now_path+'\\'+origin_name,now_path+'\\'+rename)
        
print(f'{e_cnt}개 수정 {m_cnt}개 삭제 ')
import os
import shutil
import natsort
import pandas as pd

now_path = r'C:\Users\goback\Downloads\lpr\라벨링\exp7\one_line'
file_path = now_path + '\\trash'
file_list = os.listdir(now_path)
file_name = [file for file in file_list if file.endswith('.csv')]
file_jpg = [file for file in file_list if file.endswith('.jpg')]
# file_jpg = natsort.natsorted(file_jpg)
check = False
files = pd.read_csv(now_path + '\\' +file_name[0], header=0, sep=',')
# files = files.sort_values(['날짜','흥'])
m_cnt, e_cnt, n_cnt = 0,0,0 # 삭제한 파일 갯수, 수정한 파일 갯수, 넘버링
edit, move_name, length_check, error_check = 0,0,0,0
colum = []

if '수정파일명' in files.columns : colum = ['날짜', '생성파일명', '수정파일명', '검증']
else : colum = ['날짜', '흥', '정답', '검증']

# for idx, row in files.iterrows():
#     length_check = length_check + 1 
#     folderfile = file_jpg[idx].split('.')
#     csv_num = row[colum[0]] + row[colum[1]] 
#     if folderfile[0] != csv_num :
#         error_check+=1
        # print(f'폴더파일명: {folderfile[0]} \n엑셀파일명: {csv_num}')
if error_check > 10 : file_jpg = natsort.natsorted(file_jpg)
if len(file_jpg) != length_check : print(f'엑셀파일 수정, 파일개수 {len(file_jpg)} 엑셀 행수 : {length_check}')

if not os.path.isdir(file_path): os.mkdir(file_path)

for idx, row in files.iterrows():
    
    if type(row[colum[2]]) == float : 
        move_name = file_jpg[idx]
        try :
            shutil.move(now_path +'\\'+ move_name, file_path +'\\'+ move_name)
            m_cnt = m_cnt + 1
        except :
            print(f'error : {move_name}')
        finally: continue
    elif row[colum[3]] == 1 : continue 
    elif row[colum[3]] == 0 and type(row[colum[2]]) == str :
        origin = file_jpg[idx]
        edit = row[colum[0]] + row[colum[2]] + '.jpg'
        while os.path.isfile(now_path + '\\' + edit) :
            n_cnt+=1
            edit = row[colum[0]] + row[colum[2]] + '_' + str(n_cnt) + '.jpg'
            # print(edit)
        try:
            os.rename(now_path+'\\'+origin,now_path+'\\'+edit)
            n_cnt = 0
        except Exception as e: print(e)
        finally : e_cnt = e_cnt + 1 
        
print(f'{e_cnt}개 수정 {m_cnt}개 삭제 ')
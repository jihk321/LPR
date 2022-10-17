import os
import shutil
import natsort
import pandas as pd

now_path = r'C:\Users\goback\Downloads\lpr\라벨링\exp31\one_line'
now_path = r'C:\Users\goback\Downloads\lpr\라벨링\exp31\two_lines'
file_path = now_path + '\\trash'
file_list = os.listdir(now_path)
file_name = [file for file in file_list if file.endswith('.csv')]
file_jpg = [file for file in file_list if file.endswith('.jpg')]
# file_jpg = natsort.natsorted(file_jpg)
check = False
files = pd.read_csv(now_path + '\\' +file_name[0], header=0, sep=',')
# files = files.sort_values(by= ['날짜', '흥'], ascending=[True,True])
m_cnt, e_cnt, right,n_cnt = 0,0,0,0 # 삭제한 파일 갯수, 수정한 파일 갯수, 정답, 넘버링
edit, move_name, length_check, error_check = 0,0,0,0
colum = []

if '수정파일명' in files.columns : colum = ['날짜', '생성파일명', '수정파일명', '검증']
else : colum = ['날짜', '흥', '정답', '검증']

# log = open(now_path + '\\'+'log.txt','w',encoding='utf-8-sig')
# for i in file_jpg :
#     log.write(i+ '\n')
# log.close()

def errorcheck():
    for idx, row in files.iterrows():
        length_check = length_check + 1 
        folderfile = file_jpg[idx].split('.')
        csv_num = row[colum[0]] + row[colum[1]] 
        if folderfile[0] != csv_num :
            error_check+=1
            print(f'폴더파일명: {folderfile[0]} \n엑셀파일명: {csv_num}')
    if error_check > 0 : 
        print('에러 :', error_check)
        exit()
        # file_jpg = natsort.natsorted(file_jpg)
if len(file_jpg) != length_check : print(f'엑셀파일 수정, 파일개수 {len(file_jpg)} 엑셀 행수 : {length_check}')

if not os.path.isdir(file_path): os.mkdir(file_path)


for idx, row in files.iterrows():

    if type(row[colum[2]]) == float : 
        # move_name = file_jpg[idx]
        move_name = row[colum[0]] + row[colum[1]] + '.jpg'
        pre = os.path.join(now_path,move_name)
        mov = os.path.join(file_path,move_name)
        try :
            shutil.move(pre, mov)
            m_cnt = m_cnt + 1
        except Exception as e:
            print(f'error : {e} / {move_name}')
        finally: continue
    elif row[colum[3]] == 1 : 
        right+=1
        continue 
    elif row[colum[3]] == 0 and type(row[colum[2]]) == str :
        origin = row[colum[0]] + row[colum[1]] + '.jpg'
        edit = row[colum[0]] + row[colum[2]] + '.jpg'

        ori_path = os.path.join(now_path,origin)
        
        while os.path.isfile(now_path + '\\' + edit) :
            n_cnt+=1
            edit = row[colum[0]] + row[colum[2]] + '_' + str(n_cnt) + '.jpg'
            print(edit)
        try:
            chage_path = os.path.join(now_path,edit)
            os.rename(ori_path,chage_path)
            n_cnt = 0
        except Exception as e: print(e)
        finally : e_cnt = e_cnt + 1 

def remove():
    move_file = pd.DataFrame(files[files[colum[2]].isnull()])
    if not os.path.isdir(file_path): os.mkdir(file_path)
    for idx, row in move_file.iterrows():

        move_name = str(row[colum[0]]) + str(row[colum[1]]) + '.jpg'

        try :
            shutil.move(now_path +'\\'+ move_name, file_path +'\\'+ move_name)
            m_cnt = m_cnt + 1
        except :
            remove_name = str(row[colum[0]])  + '0' + str(row[colum[1]]) + '.jpg'
            if os.path.isfile(now_path + '\\' + remove_name) :
                shutil.move(now_path +'\\'+ remove_name, file_path +'\\'+ remove_name)
                m_cnt = m_cnt + 1
    
def editname():
    edit_file = pd.DataFrame(files[files[colum[3]]].values == 0)

    for idx, row in edit_file.iterrows():
        day = str(row[colum[0]])
        origin_name = row[colum[0]] + row[colum[1]] + '.jpg'
        rename = day + str(row[colum[2]]) + '.jpg'

        e_cnt = e_cnt + 1
        # try :  os.rename(now_path+'\\'+origin_name,now_path+'\\'+rename)
        # except :
        #     while not os.path.isfile(now_path + '\\' + rename) :
        #         n_cnt = n_cnt + 1 
        #         rename = day = row[colum[2]] + '_' + str(n_cnt) + '.jpg'
        #         print(rename)
        #         os.rename(now_path+'\\'+origin_name,now_path+'\\'+rename)
            
        # finally : n_cnt = 0

        if os.path.isfile(now_path + '\\' + origin_name) :
            e_cnt = e_cnt + 1
            try : 
                
                rename = day + row[colum[2]] + '.jpg'
                os.rename(now_path+'\\'+origin_name,now_path+'\\'+rename)
                n_cnt = 0
            except :
                n_cnt = n_cnt + 1 
                rename = day + row[colum[2]] + '_01.jpg'
                print(day,row[colum[2]],n_cnt)
                os.rename(now_path+'\\'+origin_name,now_path+'\\'+rename)
        else : 
            if os.path.isfile(now_path + '\\' + day + '0' +row[colum[1]] +'.jpg') :
                os.rename(now_path+'\\'+day + '0' +row[colum[1]] +'.jpg',now_path+'\\'+rename)
            elif os.path.isfile(now_path + '\\' + day + '00' +row[colum[1]] +'.jpg') :
                os.rename(now_path+'\\'+day + '00' +row[colum[1]] +'.jpg',now_path+'\\'+rename)
            elif os.path.isfile(now_path + '\\' + day + '000' +row[colum[1]] +'.jpg') :
                os.rename(now_path+'\\'+day + '000' +row[colum[1]] +'.jpg',now_path+'\\'+rename)

print(f'{right}개 정답 {e_cnt}개 수정 {m_cnt}개 삭제 ')
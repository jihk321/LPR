import os
import shutil
import pandas as pd

now_path = r'C:\Users\goback\Downloads\lpr\라벨링\exp23\one_line'
# now_path = r'C:\Users\goback\Downloads\lpr\라벨링\exp22\two_lines'
file_path = now_path + '\\trash'
file_list = os.listdir(now_path)
file_name = [file for file in file_list if file.endswith('.csv')]
file_jpg = [file for file in file_list if file.endswith('.jpg')]
check = False
files = pd.read_csv(now_path + '\\' +file_name[0], header=0, sep=',')
files = files.sort_values('날짜')
m_cnt, e_cnt, n_cnt = 0,0,0 # 삭제한 파일 갯수, 수정한 파일 갯수, 넘버링
edit, move_name = 0,0

if not os.path.isdir(file_path): os.mkdir(file_path)

for idx, row in files.iterrows():

    if idx> 30 : break
    if type(row['정답']) == float : 
        move_name = file_jpg[idx]
        try :
            # shutil.move(now_path +'\\'+ move_name, file_path +'\\'+ move_name)
            m_cnt = m_cnt + 1
        except :
            print(f'error : {move_name}')
    if row['검증'] == 1 : continue 
    if row['검증'] == 0 and type(row['정답']) == str :
        origin = file_jpg[idx]
        edit = row['날짜'] + row['정답'] + '.jpg'
        if os.path.isfile(now_path + '\\' + edit):
            while check == True:
                if os.path.isfile(now_path + '\\' +row['날짜'] + row['정답'] + '_0' + str(n_cnt) + '.jpg'): n_cnt = n_cnt + 1
                elif not os.path.isfile(now_path + '\\' +row['날짜'] + row['정답'] + '_0' + str(n_cnt) + '.jpg'): check = True
            edit = row['날짜'] + row['정답'] + '_0' + str(n_cnt) + '.jpg'
            # print(edit)
        try:
            # os.rename(now_path+'\\'+origin,now_path+'\\'+edit)
            n_cnt = 0
        except Exception as e: print(e)
        finally : e_cnt = e_cnt + 1 
        check= False
    print(f'move_name: {move_name}   origin : {origin} edit : {edit}')

def remove():
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
    
def editname():
    edit_file = pd.DataFrame(files[files['검증']].values == 0)

    for idx, row in edit_file.iterrows():
        day = str(row['날짜'])
        origin_name = row['날짜'] + row['흥'] + '.jpg'
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

        if os.path.isfile(now_path + '\\' + origin_name) :
            e_cnt = e_cnt + 1
            try : 
                
                rename = day + row['정답'] + '.jpg'
                os.rename(now_path+'\\'+origin_name,now_path+'\\'+rename)
                n_cnt = 0
            except :
                n_cnt = n_cnt + 1 
                rename = day + row['정답'] + '_01.jpg'
                print(day,row['정답'],n_cnt)
                os.rename(now_path+'\\'+origin_name,now_path+'\\'+rename)
        else : 
            if os.path.isfile(now_path + '\\' + day + '0' +row['흥'] +'.jpg') :
                os.rename(now_path+'\\'+day + '0' +row['흥'] +'.jpg',now_path+'\\'+rename)
            elif os.path.isfile(now_path + '\\' + day + '00' +row['흥'] +'.jpg') :
                os.rename(now_path+'\\'+day + '00' +row['흥'] +'.jpg',now_path+'\\'+rename)
            elif os.path.isfile(now_path + '\\' + day + '000' +row['흥'] +'.jpg') :
                os.rename(now_path+'\\'+day + '000' +row['흥'] +'.jpg',now_path+'\\'+rename)

print(f'{e_cnt}개 수정 {m_cnt}개 삭제 ')
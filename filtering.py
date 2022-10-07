from asyncio.windows_events import NULL
from PIL import Image
import os
import numpy as np
import pandas as pd
import shutil

main_dir = '라벨링'
sub_dir = []
now_path = os.getcwd()
# letter = ['가','나','다','라','마','거','너','더','러','머','버','서','어','저','고','노','도','로','모','보','소','오','조','구','누','두','루','무','부','수','우','주','아','바','사','자','배','하','허','호']
letter = '가나다라마거너더러머버서어저고노도로모보소오조구누두루무부수우주아바사자배하허호'
def listdirs(main_dir) :
    for i in os.scandir(main_dir) :
        if i.is_dir(): 
            listdirs(i)
            if 'one_line' in i.path or 'two_lines' in i.path:
                if 'trash' not in i.path : sub_dir.append(os.path.join(now_path,i.path))
listdirs(main_dir) #main_dir 하위 폴더 리스트 
# print(sub_dir)

### 작업한 폴더인지 체크
# if os.path.isfile('log.txt') : 
#         with open('log.txt') as f:
#             folder = f.readlines()
#             sub_dir = set(sub_dir) - set(folder)
### 엑셀파일 
main_data = pd.DataFrame(columns={'번호판','사진크기','날짜','경로','기타'})
if os.path.isfile(now_path + '\\' + '데이터필터링.csv') : main_csv = pd.read_csv('데이터필터링.csv')  #open(now_path + '\\' + '데이터필터링.csv', "a", encoding='utf-8-sig')
else : main_data.to_csv('데이터필터링.csv',encoding="utf-8-sig", index=False)
### 데이터셋 폴더 
dataset = os.path.join(now_path,'dataset')
one_line = os.path.join(dataset,'one_line')
two_lines = os.path.join(dataset,'two_lines')
if not os.path.isdir(dataset): os.mkdir(dataset)
if not os.path.isdir(one_line): os.mkdir(one_line)
if not os.path.isdir(two_lines): os.mkdir(two_lines)
if not os.path.isdir(one_line + '\\' + 'dupli'): os.mkdir(one_line + '\\' + 'dupli')
if not os.path.isdir(two_lines + '\\' + 'dupli'): os.mkdir(two_lines + '\\' + 'dupli')

sub_data = pd.DataFrame(columns={'번호판','사진크기','날짜','경로','기타'})
csv_data = {}
for file in sub_dir :
    file_list = os.listdir(file)
    file_jpg = [file for file in file_list if file.endswith('.jpg')]
    for i in file_jpg :
        img = Image.open(file + '\\' + i)
        w, h = img.size
        img_size = w* h
        if '_' in i[-6:-4] :
            new_row = {'번호판' : i[16:-6] ,'사진크기' : img_size ,'날짜' : i[:16] ,'경로' : file, '기타' : i[-6:]}
        else :new_row = {'번호판' : i[16:-4] ,'사진크기' : img_size ,'날짜' : i[:16] ,'경로' : file, '기타' : '.jpg'}
        # check = list(i[16:-4])
        # print(check)
        # if 0 <= int(check[0]) <= 9 and 0 <= int(check[1]) <= 9 and letter in str(check[2]) and 0 <= int(check[3]) <= 9 and 0 <= int(check[4]) <9 and 0 <= int(check[5]) <= 9 and 0 <= int(check[6]) <= 9:
        # print(f'번호 {i[16:-4]} 사진크기{img_size} 날짜{i[:16]} 경로{file}')
        
        sub_data.loc[len(sub_data)] = new_row
sub_data = sub_data.sort_values(by=['번호판','사진크기'],ascending=False)
dup = sub_data.duplicated(['번호판'], keep='first')           
sub_data = pd.concat([sub_data, dup], axis=1)
sub_data.rename(columns= {0: '중복'}, inplace= True)
sub_data.to_csv('데이터필터링.csv',encoding="utf-8-sig", index=False)

log = open(now_path + '\\'+'log.txt','w',encoding='utf-8-sig')
for idx, row in sub_data.iterrows():
    path = sub_data.iloc[idx]['경로'] 

    if row['기타'] == '.jpg' :
        img_path = os.path.join(row['경로'],row['날짜']) + row['번호판'] + row['기타']
        print(row['경로'],row['날짜'],row['번호판'],row['기타'])
        copy_name = row['번호판'] + '.jpg'
    else : 
        img_path = os.path.join(row['경로'],row['날짜']) + row['번호판']  + row['기타']
        copy_name = row['번호판'] + row['날짜'] + '.jpg'
    
    if row['중복'] == False :
        sub_data.loc[idx,'중복'] = '메인' 
        if path in 'two_lines': shutil.copy2(img_path,two_lines + '\\' + copy_name)
        else: shutil.copy2(img_path,one_line + '\\' + copy_name)

    # else : 
    #     sub_data.loc[idx,'중복'] = '서브' 
    #     if path in 'two_lines' : shutil.copy2(img_path,two_lines + '\\' + 'dupli' + '\\' + copy_name)
    #     else: shutil.copy2(img_path,one_line + '\\' + 'dupli' + '\\' + copy_name)


# result = pd.concat([main_data,sub_data], ignore_index=True)

## 로그 작성
# log = open(now_path + '\\'+'log.txt', 'a', encoding='utf-8')
# for folderlist in sub_dir :
#     log.write(f'{folderlist}\n')
# log.close()
print('작업 완료')
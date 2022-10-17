import os
from numpy import dtype
import pandas as pd
from re import compile, split

main_dir = '라벨링'
sub_dir, allfile = [],[] #sub_dir : 하위폴더, allfile 모든 jpg 파일리스트
folder_list, dup, unique, tog = [],[],[],[] # folder_list 원 폴더 dup 중복개수, unique 단일, 종합 
now_path = os.getcwd()
letter = '가나다라마거너더러머버서어저고노도로모보소오조구누두루무부수우주아바사자배하허호'

folder_data = {}
def listdirs(main_dir) :
    for i in os.scandir(main_dir):
        if i.is_dir(): 
            listdirs(i)
            if 'one_line' in i.path or 'two_lines' in i.path:
                if 'trash' not in i.path : sub_dir.append(os.path.join(now_path,i.path))
listdirs(main_dir) #main_dir 하위 폴더 리스트 
dre = compile(r'(\d+)') 
sub_dir.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in split(dre,l)]) #windows 폴더 셋팅과 맞게 정렬

for folder in sub_dir : 
    file_list = os.listdir(folder)
    file_jpg = [file for file in file_list if file.endswith('.jpg')]

    folder_name = folder.split('\\')
    folder_name = folder_name[-2] + '_'+ folder_name[-1]
    
    folder_file = []
    # print(len(file_jpg))
    for pic in file_jpg :
        pic = pic[16:-4]
        if '_' in pic[-3:] :
            num = pic.count('_')
            if num > 1 : 
                char = pic.split('_')
                pic = char[0] + '_'+ char[1]
            else : pic = pic.split('_')[0]
        folder_file.append(pic) 
        
    result = list(set(folder_file))  #리스트 중복 제거
    allfile = allfile + result
    folder_data[folder_name] = sorted(result) # 

all_data = pd.DataFrame({'번호판' : allfile}).sort_values('번호판') #all 기준으로 정렬후 데이터프레임 생성
all_data = all_data.reset_index(drop=True) # 인덱스 리셋

sheet1 = pd.DataFrame(dict([ (k,pd.Series(v,dtype=pd.StringDtype())) for k,v in folder_data.items()]))
dup_data = all_data.value_counts().to_frame()
dup_data.columns = ['중복개수']
# datas = { '중복' : dup_data}
# sheet2 = pd.DataFrame(datas, )
folders = []

for name in sub_dir:
    name = name.split('\\')
    
    col_name = name[-2] + '_' + name[-1]
    folder_name = name[-2]
    folder_list.append(col_name)
    if folder_name not in folders : folders.append(folder_name)
    
    dup_count, uni_count = 0,0 # 중복개수, 단일 개수 
     
    col_data = sheet1[col_name].dropna().to_list()

    for search in col_data :
        if search in tog : dup_count += 1
        else : 
            uni_count += 1 
            tog.append(search)

    dup.append(dup_count)
    unique.append(uni_count)
    # print(col_data)
    
    # for count in range(len(folders)) : 
    #     if folder_list[count] in folders 

counting = pd.DataFrame(zip(folder_list,dup,unique), columns=['폴더명','중복개수','단일데이터'])

# sheet2 = pd.concat([counting,dup_data], axis=0)

# df2 = pd.concat([sheet1,all_data], axis=1)
# sheet2 = sheet1.groupby('exp20_one_line').count()
# print(df2.count())
# print(df2.value_counts())
# df.to_excel('data.csv',encoding="utf-8-sig", index=False, sheet_name='data')

#'원 번호판' : all_data['all'].unique() ,

# print(df2['all'].unique())
# print(df2['all'].value_counts())


writer = pd.ExcelWriter('data.xlsx')
sheet1.to_excel(writer, sheet_name='data')
counting.to_excel(writer, sheet_name='datas')
dup_data.to_excel(writer,sheet_name='alldata')
writer.save()

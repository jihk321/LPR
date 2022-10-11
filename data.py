import os
import pandas as pd

main_dir = '라벨링'
sub_dir, allfile = [],[]
now_path = os.getcwd()
letter = '가나다라마거너더러머버서어저고노도로모보소오조구누두루무부수우주아바사자배하허호'

folder_data = {}
def listdirs(main_dir) :
    for i in os.scandir(main_dir) :
        if i.is_dir(): 
            listdirs(i)
            if 'one_line' in i.path or 'two_lines' in i.path:
                if 'trash' not in i.path : sub_dir.append(os.path.join(now_path,i.path))
listdirs(main_dir) #main_dir 하위 폴더 리스트 

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

all_data = pd.DataFrame({'all' : allfile}).sort_values('all') #all 기준으로 정렬후 데이터프레임 생성
all_data = all_data.reset_index(drop=True) # 인덱스 리셋

sheet1 = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in folder_data.items()]))
# df2 = pd.concat([sheet1,all_data], axis=1)
# sheet2 = sheet1.groupby('exp20_one_line').count()
# print(df2.count())
# print(df2.value_counts())
# df.to_excel('data.csv',encoding="utf-8-sig", index=False, sheet_name='data')

#'원 번호판' : all_data['all'].unique() ,
datas = { '중복' : all_data['all'].value_counts()}
sheet2 = pd.DataFrame(datas)
# print(df2['all'].unique())
# print(df2['all'].value_counts())
writer = pd.ExcelWriter('data.xlsx')
sheet1.to_excel(writer, sheet_name='data')
sheet2.to_excel(writer, sheet_name='datas')
# all_data['all'].unique().to_excel(writer, sheet_name= 'count')

writer.save()
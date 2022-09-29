from operator import sub
import os
import pandas as pd

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

f = open(now_path + '\\' + '데이터필터링.csv', "w", encoding='utf-8-sig')
f.write('파일경로,날짜,파일명\n')

for file in sub_dir :
    file_list = os.listdir(file)
    file_jpg = [file for file in file_list if file.endswith('.jpg')]
    for i in file_jpg :
        check = list(i[16:-4])
        # print(check)
        # if 0 <= int(check[0]) <= 9 and 0 <= int(check[1]) <= 9 and letter in str(check[2]) and 0 <= int(check[3]) <= 9 and 0 <= int(check[4]) <9 and 0 <= int(check[5]) <= 9 and 0 <= int(check[6]) <= 9:
        f.write(file + ',' + i[0:16] + ',' + i[16:-4]+ '\n')
f.close()

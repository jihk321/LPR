lpr = '153호2115'
letter = '가나다라마거너더러머버서어저고노도로모보소오조구누두루무부수우주아바사자배하허호'
lpr_exam = list(lpr)


# print(len(lpr_exam))
if len(lpr_exam) == 8 :
    if 0<= int(lpr_exam[0]) <=9 and 0<= int(lpr_exam[1]) <=9 and 0<= int(lpr_exam[2]) <=9 and lpr_exam[3] in letter and 0<= int(lpr_exam[4]) <=9 and 0<= int(lpr_exam[5]) <=9 and 0<= int(lpr_exam[6]) <=9 and 0<= int(lpr_exam[7]) <=9:
        print('True')
elif len(lpr_exam) == 7 :
    if 0<= int(lpr_exam[0]) <=9 and 0<= int(lpr_exam[1]) <=9 and lpr_exam[2] in letter and 0<= int(lpr_exam[3]) <=9 and 0<= int(lpr_exam[4]) <=9 and 0<= int(lpr_exam[5]) <=9 and 0<= int(lpr_exam[6]) <=9 :
        print('True')

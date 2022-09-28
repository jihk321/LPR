from email.mime import image
import os
from PIL import Image

file_path = r'C:\Users\goback\Downloads\lpr\exp11\one_line'
file_list = os.listdir(file_path)
save_path = file_path + '//save'

if not os.path.isdir(save_path): os.mkdir(save_path)

for i in file_list :
    file_name = i

    img = Image.open(file_path + '\\' +file_name)

    r_img = img.transpose(Image.Transpose.ROTATE_180)
    save_name = save_path + '\\' + i
    r_img.save(save_name,'JPEG')
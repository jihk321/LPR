from email.mime import image
import os
from PIL import Image

file_path = r'C:\Users\goback\Downloads\lpr\lpr\two_lines'
file_list = os.listdir(file_path)
file_jpg = [file for file in file_list if file.endswith('.jpg')]
# save_path = file_path + '//save'

# if not os.path.isdir(save_path): os.mkdir(save_path)

for i in file_jpg :
    file_name = i

    img = Image.open(file_path + '\\' +file_name)

    r_img = img.transpose(Image.Transpose.ROTATE_180)
    save_name = file_path + '\\' + i
    r_img.save(save_name,'JPEG')
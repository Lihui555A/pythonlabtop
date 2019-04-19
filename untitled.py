from PIL import Image
import os
path=r'C:\Users\lihui\Desktop\一张图片两个目标'
list=os.listdir(path)
for i in list:
    filename=os.path.join(path,i)
    image=Image.open(filename)
    image=image.resize((90,75))
    image.save(os.path.join(path,'resize '+i))

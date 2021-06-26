import os,shutil
import time

with open('L6plus.txt', encoding='utf-8') as f:
    contents = f.read().split('</>\n')
    filelist = []
    for item in contents:
        index1 = item.index('sound://')+8
        index2 = item.index('.mp3') + 4
        filename = item[index1:index2]
        filelist.append(filename)

src_path='L6mp3/'
target_path='L6/'

for file in filelist:
    try:
        shutil.move(src_path+file,target_path+file) 
    except FileNotFoundError:
        with open('L6_notfound.txt', 'a', encoding='utf-8') as f:
            f.write(file+'\n')
        continue

print("Success")

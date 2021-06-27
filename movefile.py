import os,shutil
import time

with open('vocabulary.txt', encoding='utf-8') as f:
    contents = f.read().split('</>\n')
    filelist = []
    for item in contents:
        index1 = item.index('sound://voc//')+13
        index2 = item.index('.mp3') + 4
        filename = item[index1:index2]
        filelist.append(filename)

src_path='vocabulary/'
target_path='Vocabulary Webster Longman Dict/voc/'

for file in filelist:
    try:
        shutil.move(src_path+file,target_path+file) 
    except FileNotFoundError:
        with open('voc_notfound.txt', 'a', encoding='utf-8') as f:
            f.write(file+'\n')
        continue

print("Success")

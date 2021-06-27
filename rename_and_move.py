import os, shutil

path = 'D:/Downloads/MDX/backup/vocabulary_old/vocabularyMP3/' 
file_names = os.listdir(path)

with open('voc_notfound.txt', encoding='utf-8') as f:
    newnames = f.read().split('\n')

with open('vocabulary.txt', encoding='utf-8') as f:
    contents = f.read().split('</>\n')

dict = {}
for item in contents:
    index1 = item.index('\n')
    word = item[:index1]
    index2 = item.index('href="sound://voc//') +len('href="sound://voc//')
    index3 = item.index('.mp3') + 4
    filename = item[index2:index3]
    dict[filename] = word

target_path='D:/Downloads/MDX/Vocabulary Webster Longman Dict/voc/'

for item in newnames:
    try:
        index = item.index('/') + 1
        old_name = path + dict[item] + '.mp3'
        new_name = path + item[index:]
        os.rename(old_name,new_name)  
        shutil.move(new_name,target_path+item)
    except:
        with open('voc_failed.txt', 'a', encoding='utf-8') as f:
            f.write(item+'\n')
    else:
        print(f"{item}")

filename = 'LDOCE6.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read().split('</>\n')

for item in contents:
    index1 = item.index('href="sound://') + len('href="sound://')
    index2 = item.index('.mp3') + 4
    filename = item[index1:index2]+'\n'
    with open('LDOCE6_files.txt', 'a', encoding='utf-8') as f:
        f.write(filename)
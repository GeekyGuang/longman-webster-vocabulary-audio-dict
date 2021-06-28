import re
with open('简明英汉必应版-去音标.txt', encoding='utf-8') as f:
    contents = f.read().split('</>\n')

for item in contents:
    item = re.sub(r'\n`2`.*|</br>', "", item)
    with open('简明英汉必应版.txt', 'a', encoding='utf-8') as f:
        if item[-1] != '\n':
            item += '\n'
        f.write(f"{item}</>\n")

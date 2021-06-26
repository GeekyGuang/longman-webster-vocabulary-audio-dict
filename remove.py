import re

with open('L6_notfound_dedup.txt', encoding='utf-8') as f:
    contents = f.read().split('\n')

with open('L6plus.txt', encoding='utf-8') as f:
    contents_original = f.read()
   
for item in contents:
    count = contents_original.count(item)
    if count == 1:
        contents_original = re.sub(r'.*\n<a href="sound://'+item+'"></a>\n</>\n', '', contents_original)

        with open('1.txt', 'a', encoding='utf-8') as f:
            f.write(f"{item}\n")
    elif count > 1:
        index = contents_original.index(item) + len(item)
        front_half = contents_original[:index]
        end_half = re.sub(r'.*\n<a href="sound://'+item+'"></a>\n</>\n', '', contents_original[index:])
        contents_original = front_half + end_half

        with open('2.txt', 'a', encoding='utf-8') as f:
            f.write(f"{item}\n")

with open('L6_plus_final.txt', 'w', encoding='utf-8') as f:
    f.write(contents_original)
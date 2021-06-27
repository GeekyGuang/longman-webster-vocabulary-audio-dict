import re

with open('duplica_audio.txt', encoding='utf-8') as f:
    contents = f.read().split('\n')

with open('webster.txt', encoding='utf-8') as f:
    contents_original = f.read().split('</>\n')

print(len(contents_original))
print(len(contents))


backup = []
i = 0
for item2 in contents_original:
    i += 1
    print(i)
    for item in contents:
        if item in item2:
            backup.append(item2)
            break

print(len(backup))

for item in backup:
    contents_original.remove(item)


with open('webster2.txt', 'a', encoding='utf-8') as f:
    for item in contents_original:
        f.write(f"{item}</>\n")

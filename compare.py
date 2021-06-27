with open('vocabularyMP3.txt', encoding='utf-8') as f:
    v1 = f.read().split('</>\n')

listOld = []
for item in v1:
    index = item.index('\n')
    listOld.append(item[:index])

with open('vocabulary.txt', encoding='utf-8') as f:
    v2 = f.read().split('</>\n')

listnew = []
for item in v2:
    index = item.index('\n')
    listnew.append(item[:index])

for item in listnew:
    if item in listOld:
        listOld.remove(item)

with open('notIn.txt', 'a', encoding='utf-8') as f:
    for item in listOld:
        f.write(f'{item}\n')

print("succeed!")
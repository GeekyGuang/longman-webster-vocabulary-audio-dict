import json

with open('repulica_audio.txt', encoding='utf-8') as f:
    filenames = f.read().split('\n')

dict = {}

with open('webster_plus.txt', encoding='utf-8') as f:
    contents = f.read().split('</>\n')

for filename in filenames:
    for item in contents:
        index = item.index('\n')
        word = item[:index]
        if filename in item:
            i = dict.get(filename)
            if i:
                dict[filename].append(word)
            else:
                dict[filename] = [word]

dict2 = {}
for key, value in dict.items():
    arr = []
    for item in value:
        arr.append(item[-1])
    print(arr)
    for i in arr:
        if arr.count(i) == 1:
            dict2[key] = value
            break
        

with open('duplica_dict.json', 'w') as f:
    json.dump(dict2, f) 

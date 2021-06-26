import os

start = 'D:/Downloads/MDX/Merriam'

filenames = []

with open('MWDOnline.txt', encoding='utf-8') as f:
    contents = f.read().split('</>\n')
    for item in contents:
        index1 = item.index("sound://") + 7
        if '.wav"' in item:
            index2 = item.index(".wav") + 4
        else:
            index2 = item.index(".mp3") + 4
        file = item[index1:index2]
        filenames.append(file)

i = 0
for name in filenames:
    i += 1
    print(f"loop: {i}")

    index = name.rindex('/')+1
    path = start+name[:index]
    filename = name[index:]

    for relpath, dirs, files in os.walk(path):
        if filename not in files:
            with open('audio_notfound.txt', 'a', encoding='utf-8') as f:
                f.write(name+'\n')
        break

print('success!')

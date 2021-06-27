filename = 'webster_plus.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read().split('</>\n')

audios = []
for item in contents:
    index1 = item.index('href="sound://')
    index2 = item.index('.wav"') + 4
    audio = item[index1:index2]
    audios.append(audio)

counts = {}
for item in audios:
    counts[item] = counts.get(item, 0) + 1

for key, value in counts.items():
    if value > 1:
        with open('duplica_audio.txt', 'a', encoding='utf-8') as f:
            f.write(f"{key}\n")

print("succeed!")
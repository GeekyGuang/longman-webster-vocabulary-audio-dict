import re

with open('repulica_audio.txt', encoding='utf-8') as f:
    contents = f.read().split('\n')

with open('MWDOnline.txt', encoding='utf-8') as f:
    contents_original = f.read()
   
for item in contents:
    count = contents_original.count(item)
    if count > 1:
        index = contents_original.index(item) + len(item)
        front_half = contents_original[:index]
        end_half = re.sub(r'.*\n<a '+item+'"></a>\n</>\n', '', contents_original[index:])
        contents_original = front_half + end_half

        with open('audio_removed.txt', 'a', encoding='utf-8') as f:
            f.write(f"{item}\n")

with open('MWDOnline_re.txt', 'w', encoding='utf-8') as f:
    f.write(contents_original)
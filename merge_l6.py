with open('L6_final.txt', encoding='utf-8') as f:
    vocabulary = f.read().split('</>\n')
    vocabulary_words = []
    for item in vocabulary:
        index = item.index('\n')
        word = item[:index]
        vocabulary_words.append(word)

with open('MWDOnline.txt', encoding='utf-8') as f:
    MWDOnline = f.read().split('</>\n')
    MWDOnline_words = []
    for item in MWDOnline:
        index = item.index('\n')
        word = item[:index]
        MWDOnline_words.append(word)

for item in vocabulary_words:
    if item not in MWDOnline_words:
        index = vocabulary_words.index(item)
        with open('L6plus.txt', 'a', encoding='utf-8') as f:
            f.write(vocabulary[index]+'</>\n')

"""
for item in vocabulary_words:
    i = vocabulary_words.index(item)
    if item not in vocabulary[i]:
        print("whoops")
"""
print("Sucess!")


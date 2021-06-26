words = []
with open('MWDOnline.txt', encoding='utf-8') as f:
    contents = f.read().lower().split('</>\n')

for item in contents:
    try:
        index = item.index('\n')
    except:
        print(item)
    else:
        word = item[:index]
        words.append(word)

words_count = {}
for word in words:
    words_count[word] = words_count.get(word, 0) + 1

for key, value in words_count.items():
    if value > 1:
        with open('count.txt', 'a', encoding='utf-8') as f:
            f.write(f"{key} {value}\n")

print("success")

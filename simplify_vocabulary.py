filename = 'Vocabulary.com Dictionary 2020.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read().split('</>\n')
    for item in contents:
        index1 = item.index('\n')
        word = item[:index1]
        try:
            index2 = item.index('href="sound://')
            index3 = item.index('.mp3"', index2) + 5
        except: 
            sound = '<a href="#"></a>'
        else:
            sound = '<a ' + item[index2:index3] + '></a>'
        
        with open('vocabulary.txt', 'a', encoding='utf-8') as f:
            f.write(f"{word}\n{sound}\n</>\n")
        
print("succeed!")
            
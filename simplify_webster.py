filename = 'MW2020Pronunciation.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read().split('</>\n')
    for item in contents:
        index1 = item.index('\n')
        word = item[:index1]

        index5 = item.index('<span class="keyword">') + len('<span class="keyword">'+word)
        try:
            index6 = item.index(f"{word}<", index5) + len(word)
        except:
            try:
                index2 = item.index('href="sound://')
                index3 = item.index('.wav"', index2) + 5
            except: 
                sound = '<a href="#"></a>'
            else:
                sound = '<a ' + item[index2:index3] + '></a>'
        else:
            try:
                index2 = item.index('href="sound://',index6)
                index3 = item.index('.wav"', index2) + 5
            except: 
                sound = '<a href="#"></a>'
            else:
                sound = '<a ' + item[index2:index3] + '></a>'
        
        with open('webster.txt', 'a', encoding='utf-8') as f:
            f.write(f"{word}\n{sound}\n</>\n")
        
print("succeed!")
            
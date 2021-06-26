import re
filename = 'L6.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read()
    result = re.sub(r'.*\n<a href="#"></a>\n</>\n', '', contents)

with open('L6_final.txt', 'w', encoding='utf-8') as f:
    f.write(result)
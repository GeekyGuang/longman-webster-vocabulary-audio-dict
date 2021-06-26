filename = 'L6_notfound.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.readlines()
    dedup_contents = list(set(contents))


for item in dedup_contents:
    with open('L6_notfound_dedup.txt', 'a', encoding='utf-8') as f:
        f.write(item)

print("success")
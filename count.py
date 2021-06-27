with open('D:/Downloads/MDX/my dict/Vocabulary Webster Longman Dict.txt', encoding='utf-8') as f:
    contents = f.read().split('</>\n')

print(f"\n\nword count: {len(contents)}\n\n")
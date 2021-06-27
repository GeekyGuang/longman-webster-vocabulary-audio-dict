with open('Longman Webster Vocabulary Dict.txt', encoding='utf-8') as f:
    contents = f.read().split('</>\n')

print(f"\n\nword counts: {len(contents)}\n\n")
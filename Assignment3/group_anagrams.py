with open('words.txt', 'r') as file:
    words = [line.strip() for line in file]

anagrams = {}
for word in words:
    key = ''.join(sorted(word))
    if key not in anagrams:
        anagrams[key] = []
    anagrams[key].append(word)

with open('anagrams.txt','w') as file:
    for group in anagrams.values():
        file.write(' '.join(group) + '\n')

print("Success\nAnagrams grouped and written to anagrams.txt")

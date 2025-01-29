words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for i in range(len(words)):
    changed_el = list(words.keys())[i] * list(words.values())[i]
    print(changed_el)

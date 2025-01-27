long_str = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
words = long_str.split()

for i in range(len(words)):
    if words[i].isalpha():
        buf = words.pop(i) + "ing"
        words.insert(i, buf)
    elif words[i][-1] == "," or words[i][-1] == ".":
        buf = words[i][:-1] + "ing" + words[i][-1]
        words.pop(i)
        words.insert(i, buf)

print(*words)

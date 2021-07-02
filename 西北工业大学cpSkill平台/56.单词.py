sentence = input()
words = sentence.split(" ")
min = 10000
max = 0
max_word = ""
min_word = ""
for str in words:
    if len(str) < min:
        min_word = str
        min = len(str)
    if len(str) > max:
        max_word = str
        max = len(str)
print(min_word)
print(max_word)
        



string = input("Введите несколько слов через пробел : ")
split_word = string.split()

for num, word in enumerate(split_word, 1):
    print(num, word[:10:])
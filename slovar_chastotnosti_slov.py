words = input().split() # получим строку из пользовательского ввода и разобьем на слова
dict = {}
for word in words: # перебираем слова по одному
    if dict.get(word): # если слова есть в словаре
        dict[word] += 1 # увеличиваем счетчик количества слов на 1
    else:
        dict[word] = 1 # добавляем в словарь с количеством 1
print(dict)
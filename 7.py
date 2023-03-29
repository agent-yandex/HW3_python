# для поиска индексов напишем рекурсивную функцию
# в аргументах: слово и первый индекс вхождения = 0
def find_index_f(word, first_en=0):
    # запускаем рекурсию, пока не найдем 1-ый индекс вхождения f
    if word[0] != 'f':
        return find_index_f(word[1:], first_en + 1)
    
    return first_en


word = input()

# запускаем функцию, только если в слове есть f
if 'f' in word:
    # ищем первый индекс f в слове
    first_ind = find_index_f(word)
    # чтобы найти последний индекс, то просто переворачиваем слово
    # и ищем первый индекс f, но в уже перевернутом слове
    # затем из длины слова вычитаем индекс и еденицу, поскольку
    # индекс начинается с 0
    second_ind = len(word) - find_index_f(word[::-1]) - 1

    if first_ind == second_ind:
        print(first_ind)
    else:
        print(first_ind, second_ind)

else:
    print('Нет ни одного f в слове')






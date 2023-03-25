first_en, second_en = 0, 0 # индексы первой и последней f
# флаги: only_first - есть только 1 f, all_f - минимум 2 f
only_first, all_f = False, False
word = input()

# пробегаемся по индексам слова
for i in range(len(word)):
    let = word[i]
    if let == 'f':
        # если есть индекс первой f записываем индекс второй
        if only_first:
            second_en = i
            all_f = True
        # если нет индекса первой f
        else:
            first_en = i
            only_first = True

# по тому какой флаг определяем сколько индексов нужно вывести
if all_f:
    print(first_en, second_en)
elif only_first:
    print(first_en)

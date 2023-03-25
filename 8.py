data = [] # список для чисел
exp = input().split()
marks = "+-*"

for el in exp:
    if el not in marks:
        # добавляем число в список data
        data.append(int(el))
    else:
        # если знак операции, берем 2 числа из списка для вычисления
        # удаляя их при этом оттуда
        num2, num1 = data.pop(), data.pop()

        # в зависимости от знака производим операцию и записываем в
        # переменную res
        if el == "+":
            res = num1 + num2
        elif el == "-":
            res = num1 - num2
        elif el == "*":
            res = num1 * num2
        # теперь res - первое число
        data.append(res)

print(data[0])
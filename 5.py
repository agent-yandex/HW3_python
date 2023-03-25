data = list(map(int, input().split()))
count = 0 # количество повторяющихся пар

# проходимся по списку 2 раза:
# берем 1 элемент и пробегаемся по всему оставшемуся списку
# после этого элемента, сравнивая пары и прибавляя count,
# если пара подходящая
for i in range(len(data)):
    first = data[i]
    for j in range(i + 1, len(data)):
        if first == data[j]:
            count += 1

print(count)
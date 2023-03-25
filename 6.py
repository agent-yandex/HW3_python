def isSymmetric(data):
    # создаем список new_data по размерам равный data
    new_data = [[] for _ in range(num)]

    # в new_data запишем "перевернутый" список data
    # столбцы data будут строками в new_data
    for i in range(num):
        for j in range(num):
            new_data[i].append(data[j][i])

    # если data и new_data равные, то диагонали одинаковые
    if data == new_data:
        return 'YES'
    return 'NO'


num = int(input())
data = [list(map(int, input().split())) for _ in range(num)]

print(isSymmetric(data))
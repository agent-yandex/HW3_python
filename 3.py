data = list(map(int, input().split()))
# можно представить data как 2 части: последнее число
# и оставшиеся числа, эти части просто меняем местами
data = [data[-1]] + data[:-1]
print(*data)
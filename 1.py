def can_eat(cor1, cor2):
    # считываем координаты из введенных данных
    x1, y1 = cor1
    x2, y2 = cor2
    # конь может двигаться только на 2 клетки влево и на 1 
    # вверх, проверяем это
    if ((abs(x1 - x2) == 2 and abs(y1 - y2) == 1) 
         or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2)):
        return True
    return False

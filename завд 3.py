n = 5
shift = 4  # дополнительный сдвиг вправо для всего верхнего треугольника

# Верхний треугольник с прямым углом слева
for i in range(1, n + 1):
    print("  " * shift, end="")  # общий сдвиг вправо
    for j in range(i, 0, -1):    # числа от i до 1
        print(j, end=" ")
    print()

# Нижний треугольник (как есть)
for i in range(n, 0, -1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

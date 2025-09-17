a = int(input("Введіть a: "))
while a < 1 or a > 100:
    a = int(input("Введіть ще раз a (1..100): "))

b = int(input("Введіть b: "))

while b < 1 or b > 100:
    b = int(input("Введіть ще раз b (1..100): "))


if a > b:
    X = a / b + 31
elif a == b:
    X = -25
else:  # a < b
    X = (5 * a - 1) / a

# Результат
print("Результат обчислення виразу X:", X)


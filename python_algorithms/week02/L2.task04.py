# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

num = int(input('Введите число: '))
sum = 0
while num != 0:
    if num % 2:
        sum += 2 ** (1 - num)
    else:
        sum -= 2 ** (1 - num)
    num -= 1
print(sum)
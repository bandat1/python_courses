# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

# a. случайное целое число,
a1 = int(input('Введите число - левую границу: '))
b1 = int(input('Введите число - правую границу: '))

c1 = random.randint(a1, b1)
print(c1)

# b. случайное вещественное число,
a2 = float(input('Введите число - левую границу: '))
b2 = float(input('Введите число - правую границу: '))

c2 = random.uniform(a2, b2)
print(c2)

# c. случайный символ.
a3 = ord(input('Введите символ - левую границу: '))
b3 = ord(input('Введите символ - правую границу: '))

c3 = random.randint(a3, b3)
print(chr(c3))

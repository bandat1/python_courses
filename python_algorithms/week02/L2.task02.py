# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = input('Введите число: ')
j, k = 0, 0
for i in num:
    if int(i) % 2 == 0:
        j += 1
    else:
        k +=1
print(f'Четных чисел: {j}')
print(f'Нечетных чисел: {k}')
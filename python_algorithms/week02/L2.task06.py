# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.

import random

a = random.randint(0, 101)
n = 1 # Счетчик попыток
print(a)

while n <= 10:
    num = int(input('Введите число от 0 до 100: '))
    if num == a:
        print(f'Верно! Вы угадали число с {n}-й попытки.')
        break
    elif num > a:
        num = print(f'Попытка №{n}. Введенное число больше.')
    elif num < a:
        num = print(f'Попытка №{n}. Введенное число меньше.')

    n += 1

else:
    print(f'Вы не справились за {n-1} попыток. Загаданное число = {a}')

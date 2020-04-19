# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = [[0 for _ in range(4)] for _ in range(5)] # формируется матрица 5х4 из нулей

for i in range(0,5): # здесь формируется матрица данными от пользователя
    for j in range(0, 3):
        elem = int(input('Введите элемент матрицы: '))
        matrix[i][j] = elem

line = 0
for i in matrix:
    sum_line = 0
    for item in i:
        sum_line += item # рассчитывает значение последнего элемента для каждой строки

    matrix[line][3] = sum_line
    line += 1

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
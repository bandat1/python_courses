# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

for i in range(32, 128):
    if i % 10 == 2:
        print()
    print(f'{i:>10} - {chr(i)}', end='')

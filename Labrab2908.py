'''Задание 1
Пользователь вводит с клавиатуры два числа. Нужно показать все числа в указанном диапазоне.
Задание 2
Пользователь вводит с клавиатуры два числа. Нужно показать все нечетные числа в указанном диапазоне.
Задание 3
Пользователь вводит с клавиатуры два числа. Нужно показать все четные числа в указанном диапазоне.
Задание 4
Пользователь вводит с клавиатуры два числа. Нужно показать все числа в указанном диапазоне в порядке убывания.
Задание 5
Пользователь вводит с клавиатуры два числа. Нужно показать все нечетные числа в указанном диапазоне.
Если границы диапазона указаны неправильно требуется произвести нормализацию границ.
Например, пользователь ввел 33 и 13, требуется нормализация после которой начало диапазона станет равно 13, а конец 33.'''
#Задание № 1
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
print('Числа в этом диапазоне: ')
for z in range(x, y + 1):
    print (z, end =' ')
print ()
#Задание № 2
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
print('Нечетные числа в этом диапазоне: ')
for z in range(x, y + 1):
    if z % 2 != 0:
        print(z, end =' ')
print ()
#Задание № 3
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
print('Четные числа в этом диапазоне: ')
for z in range(x, y + 1):
    if z % 2 == 0:
        print(z, end =' ')
print ()
#Задание № 4
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
print('Числа в этом диапазоне в порядке убывания: ')
for z in range(x, y - 1, - 1):
    print (z, end =' ')
print ()
#Задание № 5
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
print('Нечетные числа в этом диапазоне: ')
if y < x:
    a = y
    b = x
else:
    a = x
    b = y
for z in range(a, b + 1):
    if z % 2 != 0:
        print(z, end=' ')


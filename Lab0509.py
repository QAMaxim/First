'''Задание 1
Пользователь вводит с клавиатуры размер стороны квадрата. Требуется отобразить на экран заполненный
квадрат. Размер стороны равен введённому размеру. Например, если пользователь ввёл 3 на экране будет выведено:
***
***
***
Задание 2
Пользователь вводит с клавиатуры ширину и высоту прямоугольника. Требуется отобразить на экран
заполненный прямоугольник с указанными высотой и шириной. Например, если пользователь ввёл высоту 3,
а ширину 5 на экране будет выведено:
*****
*****
*****
Задание 3
Пользователь вводит с клавиатуры размер стороны
квадрата. Требуется отобразить на экран незаполненный квадрат (отображаются только границы квадрата).
Размер стороны равен введённому размеру.
Задание 4
Пользователь вводит с клавиатуры длину и ширину прямоугольника.
Требуется отобразить на экран незаполненный прямоугольник (отображаются только границы прямоугольника).
Размер длины и ширины равен введенным данным.
'''
#Задание № 1
x = int(input('Введите размер стороны Вашего квадрата: '))
for z in range(x):
    for w in range(x):
        print('*', end=' ')
    print()
#Задание № 2
x = int(input('Введите высоту Вашего прямоугольника: '))
y = int(input('Введите ширину Вашего прямоугольника: '))
for z in range(x):
    for w in range(y):
        print('*', end=' ')
    print()
#Задание № 3
x = int(input('Введите размер стороны Вашего квадрата: '))
for i in range(x):
    for j in range(x):
        if i == 0 or j == 0 or i == x-1 or j == x-1:     #по аналогии с первым заданаием, но с уточнением первой(ого) и
            print("#",end=" ")                           #последней(ого) строки и столбца
        else:
            print(" ",end=" ")
    print("")
#Задание № 4
x = int(input('Введите высоту Вашего прямоугольника: '))
y = int(input('Введите ширину Вашего прямоугольника: '))
for i in range(x):
    for j in range(y):
        if i == 0 or j == 0 or i == x-1 or j == y-1:    #по аналогии со вторым заданаием, но с уточнением первой(ого) и
            print("#",end=" ")                          #последней(ого) строки и столбца
        else:
            print(" ",end=" ")
    print("")

'''Задание 1
Напишите программу, которая запрашивает два целых числа x и y, после чего вычисляет и выводит значение x в степени y.
Задание 2
Подсчитать количество целых чисел в диапазоне от 100 до 999 у которых есть две одинаковые цифры.
Задание 3
Подсчитать количество целых чисел в диапазоне от 100 до 9999 у которых все цифры разные.
Задание 4
Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6 и
вывести обратно на экран. '''
#Задание № 1
x = int(input('Введите первое целое число (х): '))
y = int(input('Введите второе целое число (у): '))
print ('Значение Вашего числа х в степени у: ', x**y)
#Задание № 2
count = 0                   #ввожу счетчик для записи получившихся по условиям задания чисел
for x in range(100, 1000):  #запускаю цикл в необходимом диапазоне (1000 потому что последнее число диапазона 999)
    z1 = x // 100           #вычленяю каждое цифру отдельно в каждом числе диапазона
    z2 = x // 10 % 10
    z3 = x % 10
    if z1 == z2 or z2 == z3 or z1 == z3 : #ввожу условие согласно задания
        count = count + 1                 #и присваиваю счетчику новые значения, которые удовлетворяют условиям задания
print('Количество целых чисел в диапазоне от 100 до 999 с двумя одинаковыми цифрами: ', count)
#Задание № 3
count1 = 0                 #ввожу счетчик для трехзначных чисел
count2 = 0                 #ввожу счетчик для четырехзначных чисел
for x in range(100, 10000):#запускаю цикл для диапазона согласно условиям задания (10000 потому что последнее число цикла 9999)
    z1 = x // 1000         #вычленяю первое и последующие числа с помощью операторов целочисленное деление и остаток
    z2 = x // 100 % 10
    z3 = x // 10 % 10
    z4 = x % 10
    if x < 1000 and z2 != z3 and z2 != z4 and z3 != z4:  #ввожу условие согласно заданию для счетчика трехзначных чисел
        count1 = count1 + 1                              #и присваиваю соответствующему счетчику новое значение
    if x >= 1000 and z1 != z2 and z1 != z3 and z1 != z4 and z2 != z3 and z2 != z4 and z3 != z4:#аналогично для 4-значных чисел
        count2 = count2 + 1
print('Количество целых чисел в диапазоне от 100 до 9999 у которых все цифры разные:', count1 + count2)

#Задание № 4
x = int(input('Введите целое число: '))
y = str(x)                                    #перевожу в тип данных "строка" для извлечения 3 и 6
a = ''                                        #ввел переменную для получившегося после удаления 3 и 6 значения
for z in y:                                   #запускаю цикл для переменной Y
    if z == '3' or z == '6' :                 #если есть значение 3 или 6
        continue                              #пропускаю их
    a = a + z                                 #и присваиваю получившееся в результает значение переменной а
x = int(a)                                    #присваиваю изначальному х новое значение в виде целого числа
print('Ваше число после удаления цифр 3 и 6:', x)
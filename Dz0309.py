'''Задание 1
Пользователь вводит с клавиатуры два числа. Нужно посчитать отдельно сумму четных, нечетных и чисел,
кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы
Задание 2
Пользователь вводит с клавиатуры длину линии и символ для заполнения линии. Нужно отобразить на
экране вертикальную линию из введенного символа, указанной длины.
Например, если было введено 5 и символ %, тогда вывод на экран будет такой:
%
%
%
%
%
Задание 3
Пользователь вводит с клавиатуры числа. Если число больше нуля нужно вывести надпись «Number is positive»,
если меньше нуля «Number is negative», если равно нулю «Number is equal to zero». Когда пользователь вводит число 7
программа прекращает свою работу и выводит на экран надпись «Good bye!»
Задание 4
Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум, введенных чисел.
Когда пользователь вводит число 7 программа прекращает свою работу и выводит на экран надпись «Good bye!'''
#Задание № 1
x = int (input('Введите первое число: '))
y = int (input('Введите второе число: '))
s2 = 0                           #ввел переменную для четных
s3 = 0                           #ввел переменную для нечетных
s9 = 0                           #ввел переменную для кратных 9
count2 = 0                       # счетчик четных для подсчета среднеарифметического
count3 = 0                       # счетчик нечетных
count9 = 0                       # счетчик кратных 9
for z in range (x, y, + 1) :     # запускаю цикл в диапазоне пользователя с шагом +1
    if z % 2 == 0 :              # проверяю на четность с помощью оператора "остаток"
        s2 = z + s2              # вычисляю сумму четных чисел
        count2 = count2 + 1      # присваиваю счетчику четных чисел значение количества чисел в диапазоне
    if z % 2 != 0 :              # проверяю на нечетность с помощью оператора "остаток"
        s3 = z + s3              # вычисляю сумму нечетных чисел
        count3 = count3 + 1      # присваиваю счетчику нечетных чисел значение количества чисел в диапазоне
    if z % 9 == 0 :              # проверяю на кратность 9 с помощью оператора "остаток"
        s9 = z + s9              # вычисляю сумму кратных 9 чисел
        count9 = count9 +1       # присваиваю счетчику кратных 9 чисел значение количества чисел в диапазоне
print ('Сумма четных чисел в указанном Вами диапазоне: ', s2)              #вывожу на экран сумму четных чисел диапазона
print ('Среднеарифметическое группы четных чисел в диапазоне: ', s2/count2)#вывожу на экран среднеарифметическое четных
print ('Сумма нечетных чисел в указанном диапазоне: ', s3,)                #вывожу на экран сумму нечетных
print ('Среднеарифметическое группы нечетных чисел в диапазоне: ', s3/count3)#вывожу на экран среднеарифметическое нечетных
print ('Сумма чисел кратных 9 в указанном диапазоне: ', s9)                #вывожу на экран сумму кратных 9
print ('Среднеарифметическое группы кратных 9 чисел в диапазоне: ', s9/count9)#вывожу на экран среднеарифметическое кратных 9
#Задание № 2
x = int (input('Введите длину линии: '))                     #ввод пользователем длины
y = (input('Из какого символа вывести длину Вашей линии? ')) #ввод пользователем символа для отображения
for z in range (x) :                                         #запускаю цикл for (для) в диапазоне пользователя
    print (y)                                                #и вывод на экран вертикально длины из символа пользователя
#Задание № 3
while True:                               #запускаю цикл с условием "пока" истина
    x = int (input('Введите число: '))    #ввод числа пользователем
    if x > 0 and x != 7:                  #условие обязательно в виде х больше 0 и не ровно 7 в соответствии с условиями
        print ('Number is positive')
    elif x < 0:                           #условие однако (также) если х меньше 0
        print ('Number is negative')
    elif x == 0:                          #условие однако (также) если x равен 0
        print ('Number is equal to zero')
    if x == 7:                            #условие если x равен 7
        print ('Good bye!')
        break                             #вывод на экран по условиям задания и прерывание цикла
#Задание № 4
x = int (input('Введите число: '))        #ввод пользователем числа
s = 0                                     #ввожу переменную для суммы чисел
ma = x                                    #ввожу переменную для вычисления максимального числа и присваиваю значение x
mi = x                                    #ввожу переменную для минимального числа (именно для этого сделал ввод x)
while True :                              #запускаю цикл while ("пока") истина
    if x == 7 :                           #условие по требованиям задания если х равен 7
        print ('Good bye!')               #вывод на экран по требованиям задания
        break                             #и прерывание цикла
    s = s + x                             #сразу вычисляю сумму (если одно число, то сумма 7)
    if x > ma :                           #условие если для вычисления максимального числа
        ma = x                            #и присваивание этого значение соответствующей переменной
    elif x < mi :                         #условие однако (также) для вычисления мнимального числа
        mi = x                            #и присваивание этого значения соответствующей переменной
    x = int(input('Введите число: '))     #ввод числа внутри цикла чтобы все работало. Для пользователя это "за кадром".
print ("Максимальное число: ", ma)
print ("Миимальное число: ", mi)
print ('Сумма чисел введеных Вами: ', s)

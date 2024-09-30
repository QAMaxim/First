'''Задание 1
Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
“Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself.”
Bill Gates
Задание 2
Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа между ними.
Задание 3
Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой.
Задание 4
Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров.
Задание 5
Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
передаются в качестве параметров. Если границы диапазона перепутаны (например, 5 - верхняя граница, 25 - нижняя граница),
их нужно поменять местами.
Задание 6
Напишите функцию, которая считает количество цифр в числе. Число передаётся в качестве параметра. Из
функции нужно вернуть полученное количество цифр. Например, если передали 3456, количество цифр будет 4.
Задание 7
Напишите функцию, которая проверяет является ли число палиндромом. Число передаётся в качестве параметра.
Если число палиндром нужно вернуть из функции true, иначе false.
«Палиндром» — это число, у которого первая часть цифр равна второй перевернутой части цифр. Например,
123321—палиндром(первая часть 123, вторая 321, которая после переворота становится 123), 546645 — палиндром,
а 421987 — не палиндром.'''
#Задание №1
def gates () :                                                          #создаю новую функцию с пустым аргументом и задаю имя
    print ('''“Don't compare yourself with anyone in this world…''')    #для вывода на экран применил руное
    print ('''if you do so, you are insulting yourself.”''')            #форматирование, без методов и параметров
    print ('''                                       Bill Gates.''')
gates()                                                                 #вывожу на экран функцию (вызываю)
#Задание №2
def ch (x1, x2):                                #создаю новую функцию, задаю имя функции и два аргумента
    y = min(x1, x2)                             #вычисляю минимальное значение
    z = max(x1, x2)                             #аналогично вычисляю максимальное значение
    print(f"Четные числа между {y} и {z}:")
    for n in range(y, z + 1):                   #запускаю цикл для вычисления четных в диапазоне аргументов с шагом +1
        if n % 2 == 0:                          #ввожу условие
            print(n)                            #и при его исполнении вывожу на экран значение
ch (3, 10)                               #вызываю функцию с указанием необходимых аргументов
#Задание №3
def kv(x, y, z):                            #создаю функцию, задаю ей имя и три необходимых аргумента
    if z:                                   #ввожу ветвление с условием если аргумент истина
        print("Заполненный квадрат: ")
        for k in range(x):                  #и вводом внутри ветвления цикла в радиусе аргумента функции
            print(y * x)                    #вывожу на экран фигуру согласно условиям
    else:                                   #условие когда аргумент ложь создаю аналогично тому когда аргумент истина
        print("Незаполненный квадрат: ")
        print(y * x)                        #но вывожу сплошную вержнюю сторону квадрата
        for k in range(x - 2):              #ввожу цикл внутри условия ветвления в необходимом диапазоне
            print(y + " " * (x - 2) + y)    #задаю условия для вывода пустого внутри квадрата
        print(y * x)                        #и сплошную нижнюю сторону квадрата
kv(3, "*", True)                   #вызовом созданной выше функции вывожу на экран наши квадраты
kv(3, "!", False)
#Задание №4
def mi (a, b, c, d, e):                     #создаю функцию с 5 аргументами и задаю ей имя
    return min(a, b, c, d, e)               #которая будет возвращать минимальный из аргументов
x = mi (10, 5, 8, 12, 3)     #задаю переменную, вызываю созданную функцию и ввожу 5 аргументов
print("Ваше минимальное число:", x)
#Задание №5
def proiz(x, y):                                #создаю функцию, задаю имя и два аргумента
    if x > y:                                   #задаю условие
        x, y = y, x                             #и при его возникновении меняю аргументы местами согласно условию
    p = 1                                       #ввожу новую переменную для записи результата умножения
    for z in range(x, y + 1):                   #запускаю цикл в диапазоне аргументов созданной функции с шагом +1
        p = p * z                               #перемножаю все значения внутри диапазона
    return p                                    #и записываю результат в ранее созданную переменную
a = proiz(6, 5)                           #далее создаю переменную, вызываю созданную функцию и ввожу необходимые параметры
print("Произведение чисел в введеном Вами диапазоне:", a)
#Задание №6
def sch(a):                 #создаю функцию с одним аргументом, задаю ей имя и сразу сообщаю что
    return len(str(a))      #функция должна возвращать длину аргумента предварительно переведенного в тип данных- строка
x = 3456656                 #создаю переменную для удобства вывода на экран, в которой записано значение числа
y = sch(x)                  #создаю переменную и  просто вызываю ранее созданную функцию
print(f"Количество цифр в числе {x}: {y}")  #для удобства использую формат строки
#Задание №7
def pali (a):               #создаю функцию с одним параметром и сразу сообщаю что
    x = str(a)              #необходимо в созданную переменную записать значение аргумента функции в типе данных - строка
    return x == x[::-1]     #и проверить равны ли значения слева направо и справа налево
x = 123321                  #для удобства вывода на экран создаю переменную в которой хранится значение проверяемого числа
y = pali (x)                #и просто вызываю созданную функцию
print(f"{x} является палиндромом: {y}")  #для удобства использую формат строки
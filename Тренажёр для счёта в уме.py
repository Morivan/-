import random
import time
x = 0
y = 0
w = 0
k = 0
z = 0
successe = ['Верно', 'Точно', 'Правильно', 'Да']
failure = ['Ошибка', 'Неверно', 'Неправильно', 'Нет']
a = input('Введите количество разрядов в первом числе:')
b = input('Введите количество разрядов во втором числе:')
X = input('Выберите операцию между этими числами:'
          '\nВозможные операции:\nСложение[1]\nВычитание[2]\nУмножение[3]\nДеление[4]\n'
          'p.s. Для выбора операции наберите цифру рядом с ней\n'
          'Ваш выбор:')
a = int(a)
b = int(b)
t1 = time.time()
if X == '1':
    X = '+'
    x = (random.randrange(10 ** (a - 1), 10 ** a))
    y = (random.randrange(10 ** (b - 1), 10 ** b))
    w = x + y
    z = input(str(x) + '+' + str(y) + '=')
elif X == '2':
    x = (random.randrange(10 ** (a - 1), 10 ** a))
    y = (random.randrange(10 ** (b - 1), 10 ** b))
    if x < y:
        w = y - x
        z = input(str(y) + '-' + str(x) + '=')
    else:
        w = x - y
        z = input(str(x) + '-' + str(y) + '=')
    X = '-'
elif X == '3':
    x = (random.randrange(10 ** (a - 1), 10 ** a))
    y = (random.randrange(10 ** (b - 1), 10 ** b))
    w = x * y
    z = input(str(x) + '*' + str(y) + '=')
    X = '*'
elif X == '4':
    x = a
    y = b
    if x > y:
        x = (random.randrange(10 ** (a - 1), 10 ** a))
        y = (random.randrange(10 ** (b - 1), 10 ** b))
        while not (x % y == 0) or (x == y):
            x = (random.randrange(10 ** (a - 1), 10 ** a))
            y = (random.randrange(10 ** (b - 1), 10 ** b))
        w = x / y
        z = input(str(x) + '/' + str(y) + '=')
    else:
        x = (random.randrange(10 ** (a - 1), 10 ** a))
        y = (random.randrange(10 ** (b - 1), 10 ** b))
        while not (y % x == 0) or (x == y):
            x = (random.randrange(10 ** (a - 1), 10 ** a))
            y = (random.randrange(10 ** (b - 1), 10 ** b))
        w = y / x
        z = input(str(y) + '/' + str(x) + '=')
    X = '/'
else:
    print('Необходимо вбить цифру в скобках')
if int(z) == w:
    k = 'Да'
    print(successe[random.randrange(0, 3)])
else:
    k = 'Нет'
    print(failure[random.randrange(0, 3)])
t2 = time.time()
t3 = str(round(t2-t1, 2))
f1 = open('Результаты.txt', 'a')
if x >= y:
    f1.write('На выражение:' + str(x) + X + str(y) + ' был дан ответ ' + str(w) + ' за ' + t3
             + ' секунд. Верный ли ответ? ' + str(k) + '\n')
else:
    f1.write(
        'На выражение:' + str(y) + X + str(x) + ' был дан ответ ' + str(w) + ' за ' + t3 +
        ' секунд. Верный ли ответ? ' + str(k) + '\n')
f1.close()
input('На ответ потребовалось приблизительно ' + str(int(t2-t1))+' секунд')

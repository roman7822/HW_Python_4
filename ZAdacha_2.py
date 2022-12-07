n = int(input('Введите число N: '))
lst = []
a = n
if n > 1:
    restart = True
    while restart:
        restart = False
        for i in range (2, n+1):
            if n%i == 0:
                lst.append(i)
                n = int(n/i)
                restart = True
                break
                   
    new_lst = []
    [new_lst.append(i) for i in lst if i not in new_lst]
    print(f'Простые множители числа {a} -> {lst}')
    print(f'Простые неповторяющиеся множители числа {a} -> {new_lst}')
elif n == 1:
    print(f'Простые множители числа {a} -> [1]')
else:
    print(f'Вы ввели не правильное число')
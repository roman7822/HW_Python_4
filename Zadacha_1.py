import math
x=math.pi
n=input('Введите число d чтобы задать точность вывода числа π (например: 0.001, 0,01): ')
count = 0

n = n.replace('0.', '')

for i in n:
    count+=1

print(f'Число {x:0.{count}f}')
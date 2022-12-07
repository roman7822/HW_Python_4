import sympy

from sympy import simplify


with open('file1.txt', 'r') as data1:
    st1 = data1.read()
with open('file2.txt', 'r') as data2:
    st2 = data2.read()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")

st3 = simplify(st1 + '+' + st2)
st3 = str(st3)

print(f"Результирующий многочлен {st3}")


with open('result.txt', 'w') as data:
        data.write(st3)

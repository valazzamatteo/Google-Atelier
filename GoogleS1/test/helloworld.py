"""
This is my first docstring
"""
lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(lista)
print(sorted(lista))
print(sorted(lista, reverse=True))
print(lista[::2])
print(lista[1::2])
element_divizabile_cu_3 = []
for i in lista:
    if i % 3 == 0:
        element_divizabile_cu_3.append(i)
print(element_divizabile_cu_3)

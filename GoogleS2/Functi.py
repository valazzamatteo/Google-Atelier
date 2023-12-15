def suma(*args, **kargs):
    total_sum = 0
    for a in args:
        if isinstance(a, (int, float)):
            total_sum += a
    return total_sum


def recursiv_sum(data):
    if not data:
        return 0, 0, 0
    sumat, par, impar = recursiv_sum(data[1:])
    nr = data[0]
    if nr % 2 == 0:
        par += nr
    else:
        impar += nr
    sumat += nr
    return sumat, par, impar


def citire():
    try:
     nr=int(input("Nr intreg"))
     return nr
    except ValueError:
        return 0



print(suma(1, 5, -3, 'abc', [12, 56, 'cad']))
print(suma())
print(suma(2, 4, 'abc', param_1=2))

print(recursiv_sum([1, 2, 3, 4, 5]))
print(citire())
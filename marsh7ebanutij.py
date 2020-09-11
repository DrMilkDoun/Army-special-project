Sk = float(input('Введите скорость в км/ч: '))
Sm = Sk * 50 / 3
P = Sm - int(Sm)
if P == 0:
    print(Sm)
else:
    while P <= 1:
        P *= 10
        A = int(P)
        A /= 10
    Sm = int(Sm) + A
    print(Sm)

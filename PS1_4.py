def Least_moves(x):
    a = 0
    while x != 1:
        if x % 2 == 0:
            x = x / 2
            a = a + 1
        else:
            x = (x-1)/2
            a = a + 2
    else:
        print(a)
Least_moves(2)
Least_moves(5)
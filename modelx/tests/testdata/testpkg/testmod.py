

# modfibo(10) == 55

def modfibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return modfibo(n - 1) + modfibo(n - 2)

# modbar(2) == 4

def modbar(n):
    return baz * n


baz = 2

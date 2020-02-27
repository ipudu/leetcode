# for integer

def number_swapper(a, b):
    a = a - b
    b = a + b
    a = b - a
    return a, b


# bit manipulation

def number_swapper_2(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
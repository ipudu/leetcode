#solution 1

def string_rotation(a, b):
    if len(a) != len(b):
        return False
    return b in a * 2

if __name__ == '__main__':
    print(string_rotation('waterbottle', 'erbottlewat'))
    print(string_rotation('world', 'hello'))
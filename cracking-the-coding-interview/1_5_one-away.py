#solution 1
#O(n)

def one_away(a, b):
    if abs(len(a) - len(b)) > 1:
        return False
    
    # same length
    if len(a) == len(b):
        counter = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                counter += 1
        return True if counter <= 1 else False
    
    # len1 - len2 == +-1
    if len(a) > len(b):
        a, b = b, a

    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] != b[j]:
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1
    return True

if __name__ == '__main__':
    print(one_away('pale', 'ple'))
    print(one_away('pales', 'pale'))
    print(one_away('pale', 'bale'))
    print(one_away('pale', 'bae'))
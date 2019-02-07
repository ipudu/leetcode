#solution 1
#O(n)

def check_permutation_1(a, b):
    if len(a) != len(b):
        return False
    def string_to_dict(s):
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        return d
    return string_to_dict(a) == string_to_dict(b)

#solution 2
#O(nlog(n))

def check_permutation_2(a, b):
    return sorted(a) == sorted(b)

if __name__ == '__main__':
    print(check_permutation_1('hello', 'olleh'))
    print(check_permutation_1('hello', 'world'))
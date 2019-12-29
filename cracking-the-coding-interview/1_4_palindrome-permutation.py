#solution 1
#O(n)

def palindrome_permutation(s):
    d = {}
    for c in s:
        if c != ' ':
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
    count = 0

    for k, v in d.items():
        if v % 2 == 1:
            count += 1
    if count > 1:
        return False
    else:
        return True

if __name__ == '__main__':
    print(palindrome_permutation('taco cat'))
    print(palindrome_permutation('Hello World!'))
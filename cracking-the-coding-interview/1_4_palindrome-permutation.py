#solution 1
#O(n)

def palindrome_permutation(a, b):
    return ''.join(sorted(list(a))) == ''.join(sorted(list(b)))

if __name__ == '__main__':
    print(palindrome_permutation('taco cat', 'atco cta'))
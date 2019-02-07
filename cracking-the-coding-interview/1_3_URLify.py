#solution 1
#O(n)

def URLify(s):
    l = list(s)
    for i in range(len(l)):
        if l[i] == ' ':
            l[i] = '%20'
    return ''.join(l)

if __name__ == '__main__':
    print(URLify('Hello World!'))
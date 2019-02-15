#solution 1
#O(m*n)

def zero_matrix(a):
    m = len(a)
    n = len(a[0])
    f1 = False
    f2 = False
    for row in a:
        if sum(row) == 0:
            f1 = True
            break
    for i in range(n):
        col = 0
        for j in range(m):
            col += a[j][i]
        if col == 0:
            f2 = True
            break
    return f1 and f2

if __name__ == '__main__':
    print(zero_matrix([[0,0],[0,0]]))
    print(zero_matrix([[1,0],[0,1]]))
#solution 1
#O(n)

def rotate_matrix(a):
    N  = len(a)
    for i in range(0, int(N/2)):
        for j in range(i, N-i-1):
            temp  = a[i][j]
            a[i][j] = a[j][N-1-i]
            a[j][N-1-i] = a[N-1-i][N-1-j]
            a[N-1-i][N-1-j] = a[N-1-j][i]
            a[N-1-j][i] = temp 
    return a
if __name__ == '__main__':
    a = [ [1, 2, 3, 4 ], 
          [5, 6, 7, 8 ], 
          [9, 10, 11, 12 ], 
          [13, 14, 15, 16 ] ] 

    for r in rotate_matrix(a):
        print(r)
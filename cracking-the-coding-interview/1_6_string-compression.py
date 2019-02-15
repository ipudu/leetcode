#solution 1
#O(n)

def string_compression(a):
    a = a.lower()
    if len(a) == 1:
        return a
    ans = ''
    counter = 1
    flag = False
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            counter += 1
            flag = True
        else:
            ans += a[i-1] + str(counter)
            counter = 1
    ans += a[-1] + str(counter)
    
    return ans if flag else a

if __name__ == '__main__':
    print(string_compression('helloworld'))
    print(string_compression('world'))
class MinStack:
    def __init__(self):
        self.s = [(0, float('inf'))]
    
    def push(self, n):
        if n < self.s[-1][1]:
            self.s.append((n, n))
        else:
            self.s.append((n, self.s[-1][1]))

    def pop(self):
        return self.s.pop()[0]
    
    def min(self):
        return self.s[-1][1]


if __name__ == "__main__":
    s = MinStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(-1)
    print(s.min())
    s.pop()
    print(s.min())
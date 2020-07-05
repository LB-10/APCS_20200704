class Foo:
    def __init__(self):
        self.up = 1
        self.down = 6
        self.front = 4
        self.back = 3
        self.right = 2
        self.left = 5
    def rotateRight(self):
        self.left, self.up, self.right, self.down = (self.down, self.left, self.up, self.right)
    def rotateFront(self):
        self.back, self.up, self.front, self.down = (self.down, self.back, self.up, self.front)

while True:
    try:
        n, m = (int(num) for num in input().strip().split())
    except:
        break
    else:
        foos = [Foo() for i in range(n+1)]
        for i in range(m):
            op1, op2 = (int(num) for num in input().strip().split())
            if op2 == -1:
                foos[op1].rotateFront()
            elif op2 == -2:
                foos[op1].rotateRight()
            else:
                foos[op1], foos[op2] = (foos[op2], foos[op1]) #swap
        del foos[0] # for padding only
        for foo in foos:
            print(foo.up, end=' ')
        print('') # for new line
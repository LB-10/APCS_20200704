goods = []
A = B = 0
def check(buy, a, b):
    try:
        buy.index(a)
        buy.index(b)
    except:
        return 0
    else:
        return 1
while True:
    try:
        A, B = (int(num) for num in input().strip().split())
    except:
        break
    else:
        T = int(input())
        for i in range(T):
            a = [int(num) for num in input().strip().split()]
            del a[-1] #a = [...,0]
            b = []
            for c in a:
                if c < 0:
                    b.remove(abs(c))
                else:
                    b.append(c)
            goods.append(b)
        cnt = 0
        for buy in goods:
            cnt += check(buy, A, B)
        print(cnt)
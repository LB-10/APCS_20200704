while True:
    try:
        m, n = (int(num) for num in input().strip().split())
    except:
        break
    else:
        rooms = [int(num) for num in input().strip().split()] # len:m
        keys = [int(num) for num in input().strip().split()] # len:n

        i = 0
        point = 0
        while keys:
            if point >= keys[0]:
                point = 0
                del keys[0]
            point += rooms[i]
            i = (i+1)%m
        print(i)

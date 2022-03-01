# cook your dish here
while True:
    try:
        t = input()
        while(t):
            x1, y1, x2, y2 = input().split()
            x = int(x1) - int(x2)
            y = int(y1) - int(y2)
            m = max(abs(x), abs(y))
            print(m)
    except EOFError:
        break
        
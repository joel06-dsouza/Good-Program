# cook your dish here
while True:
    try:
        t = int(input())
        while(t):
            x = int(input())
            if(x % 4 == 0):
                print("Good")
            else:
                print("Not Good")
    except EOFError:
        break
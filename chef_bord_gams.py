tc = int(input())
for i in range (0,tc):
    n = int(input())
    box = 0
    for i in range(1,n+1):
        if i%2!=0:
            box = box + (n-i+1)**2
    print(box)

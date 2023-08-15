tc = int(input())
for i in range (0,tc):
    n,a,b = map(int,input().split(" "))
    s = [0]*n
    s = list(map(int,input().split(" ")))
    ac, bc = 0,0
    for j in s:
        if j%a==0:
            ac+=1
            continue
        elif j%b==0:
            bc+=1
        else:
            continue
    print('BOB') if ac>bc else print('ALICE')

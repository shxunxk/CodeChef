tc = int(input())
for i in range (0,tc):
    b = 0
    l = 0
    a = 1
    n = int(input())
    for j in range(n,0,-1):
        for k in range(j,0,-1):
            if((k & a)>0):
                l+=1
                a=k&a
            else:
                if(l>b):
                    b=l
                break
        if(b>j):
            break
    print(b+1)
  
#partailly correct solution
#TLE

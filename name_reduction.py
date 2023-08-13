c = int(input())
for i in range(c):
    a, b = input().split(" ")
    p = a + b
    n = int(input())
    s = [""] * n
    su = ""
    c = 0
    for j in range(n):
        s[j] = input()
    for j in range(n):
        su = su + s[j]
    
    su = sorted(su)
    p = sorted(p)
    
    k = 0
    for j in range(0, len(p)):
        if k < len(su) and su[k] == p[j]:
            k = k + 1
        else:
            continue
    
    if len(su) == k:
        print("YES")
    else:
        print("NO")

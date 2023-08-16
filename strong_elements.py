import math

def calculate_solution(n, array):
    start = []
    end = []
    x, y = array[0], array[-1]
    
    for i in range(n):
        x = math.gcd(x, array[i])
        start.append(x)
    
    for i in range(n - 1, -1, -1):
        y = math.gcd(y, array[i])
        end.append(y)
    end = end[::-1]
    
    ans = 0
    if end[1] != 1:
        ans += 1
    
    for i in range(1, n - 1):
        if math.gcd(start[i - 1], end[i + 1]) != 1:
            ans += 1
    
    if start[n - 2] != 1:
        ans += 1
    
    return ans

tc = int(input())
for i in range(tc):
    array_length = int(input())
    input_array = list(map(int, input().split()))
    print(calculate_solution(array_length, input_array))

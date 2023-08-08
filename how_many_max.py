tc = int(input())
for _ in range(tc):
    size = int(input())
    string = input().strip()
    arr = [0] * (size + 1)

    for k in range(size - 1):
        if string[k] == '0':
            arr[k] = 0
            arr[k+1] = 1
        elif string[k] == '1':
            arr[k] = 1
            arr[k-1] = 0
        else:
            break

    count = 0
    for k in range(size + 1):
        if arr[k] == 1:
            count += 1
    print(count)

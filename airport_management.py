tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    d = list(map(int, input().split()))

    r = [0] * 1441

    for time in a:
        r[time] += 1
    for time in d:
        r[time] += 1

    print(max(r))

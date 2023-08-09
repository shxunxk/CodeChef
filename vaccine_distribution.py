tc = int(input())
for _ in range(tc):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    at_risk = 0
    not_at_risk = 0

    for age in a:
        if age <= 9 or age >= 80:
            at_risk += 1
        else:
            not_at_risk += 1

    days = at_risk // d + (1 if at_risk % d != 0 else 0)
    days += not_at_risk // d + (1 if not_at_risk % d != 0 else 0)

    print(days)

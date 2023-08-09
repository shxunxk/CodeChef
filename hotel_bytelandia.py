tc = int(input())

for _ in range(tc):
    n = int(input())
    arrival_times = list(map(int, input().split()))
    departure_times = list(map(int, input().split()))

    events = []
    for i in range(n):
        events.append((arrival_times[i], 1))
        events.append((departure_times[i], -1))

    events.sort()

    max_guests = 0
    current_guests = 0

    for event in events:
        current_guests += event[1]
        max_guests = max(max_guests, current_guests)

    print(max_guests)

a, b, x, y = map(int, input().split(" "))

m = 2 * a + b
r = 2 * x + y

print('Messi') if m > r else print('Ronaldo') if r > m else print('Equal')

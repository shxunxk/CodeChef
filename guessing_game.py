def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
def calc_prob(n, m):
    total_pairs = n * m
    odd_pairs = (n // 2) * (m // 2) + ((n + 1) // 2) * ((m + 1) // 2)
    even_pairs = total_pairs - odd_pairs
    return odd_pairs, even_pairs, total_pairs

tc = int(input())
for i in range(tc):
    n, m = map(int, input().split(" "))
    
    odd, even, den = calc_prob(n,m)
    
    res = gcd(odd, den)
    odd = odd//res
    den = den//res
    
    print(str(odd) + "/" + str(den))
  
# the followinng code has a minor error

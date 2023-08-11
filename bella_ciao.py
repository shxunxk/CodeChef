*** less efficient code (partially correct)***

# tc = int(input())
# for i in range(tc):
#     td, d, p, q = map(int, input().split(" "))
#     total = 0
#     j = -1
#     for k in range(0, td):
#         if k % d == 0:
#             j += 1
#         total = total + p + j * q
#     print(total)

*** More efficient code ***

tc = int(input())
for i in range(tc):
    td, d, p, q = map(int, input().split(" "))
    
    comp_int = td // d
    remd = td % d
    
    total_in_int = (d*(2*p + (comp_int - 1)*q))* comp_int // 2
    total_in_rem = (p + comp_int*q)*remd
    
    total = total_in_int + total_in_rem
    
    print(total)

tc = int(input())
earn = []
tax = []
for i in range(0, tc):
    temp=input().split(" ")
    earn.append(int(temp[0]))
    tax.append(int(temp[1]))
for i in range(0, tc):
    print(int(earn[i]-tax[i]))

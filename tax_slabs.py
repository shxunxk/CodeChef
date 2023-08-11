tc = int(input())
for i in range(tc):
    inc = int(input())
    
    tax = 0
    
    if inc > 250000:
        if inc >= 500000:
            tax = tax + (250000) * 0.05
        else:
            tax = tax + 0.05 * (inc - 250000)
    if inc > 500000:
        if inc >= 750000:
            tax = tax + (250000) * 0.1
        else:
            tax = tax + 0.1 * (inc - 500000)
    if inc > 750000:
        if inc >= 1000000:
            tax = tax + (250000) * 0.15
        else:
            tax = tax + 0.15 * (inc - 750000)
    if inc > 1000000:
        if inc >= 1250000:
            tax = tax + (250000) * 0.20
        else:
            tax = tax + 0.20 * (inc - 1000000)
    if inc > 1250000:
        if inc >= 1500000:
            tax = tax + (250000) * 0.25
        else:
            tax = tax + 0.25 * (inc - 1250000)
    if inc > 1500000:
        tax = tax + 0.3 * (inc - 1500000)
    
    net_income = inc - tax
    print(round(net_income))

***the code can be solved with shorter logic as well so it can be solved in more efficient way than this***

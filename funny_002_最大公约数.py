a = 3
b = 5
m = min(a, b)
for x in range(m,0,-1):
    if a%x ==0 and b%x==0:
        print(x)
        break

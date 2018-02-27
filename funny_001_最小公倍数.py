a = 3
b = 5
m = max(a, b)
for x in range(m, a*b+1):
    if x%a == 0 and x%b== 0:
        print(x)
        break

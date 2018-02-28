# 我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。今天我们反其道而行之，给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。输出这两个数，小的在前，大的在后，以空格隔开。若有多组解，输出它们之和最小的那组。注：所给数据都有解，不用考虑无解的情况。
#
# 例如：a=3, b = 60
#
# 则输出：12 15
def min_num(a,b):
    m = max(a, b)
    for x in range(m, a * b + 1):
        if x % a == 0 and x % b == 0:
            return x


def max_num(a,b):
    m = min(a, b)
    for x in range(m, 0, -1):
        if a % x == 0 and b % x == 0:
            return x

a = 3
b = 60


for x in range(a, int(b/a)):
    for y in range (x+1,int(b/a)+1):
        #print(x,y)
        if min_num(x,y) == b and max_num(x,y) ==a :
            print("%d %d" %(x, y))
            brea

a = 5
n = 20132013

def power_mod(a,b,c):
    """大幂取余数，时间复杂度O(n)

    :param a:底数
    :param b:指数
    :param c:取余数
    :return:返回结果
    """
    ans = 1
    for i in range(0,b):
        ans = (ans*a) % c
    return ans

def quick_mod(a, b, c):
    """大幂数取余函数

    :param a:底数
    :param b:指数
    :param c:取余数
    :return:返回值
    """
    ans = 1
    while(b):
        if b%2 == 1:
            ans = (ans*a) % c
        b /= 2
        a = (a*a) %c
    return ans

# 描述:
# 把一个偶数拆成两个不同素数的和，有几种拆法呢？
# 现在来考虑考虑这个问题，给你一个不超过10000的正的偶数n，
# 计算将该数拆成两个不同的素数之和的方法数，并输出。
# 如n=10，可以拆成3+7，只有这一种方法，因此输出1.



def is_prime(x):
    """判断一个整数是不是素数

    :param x:整数
    :return:返回bool类型
    """
    if x < 2:
        return False
    elif x in [2,3]:
        return True
    else:
        for i in range(2, int(x/2)):
            if x % i == 0:
                return False
        else:
            return True

n = 10
flag = 0
for i in range(2,int(n/2)):
    if is_prime(i) and is_prime(n-i):
        flag += 1

print(flag)

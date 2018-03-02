# 采用两种法师计算斐波那契数列
# 1.递归法
# 2.动态规划
import time

def fibonaccin_recursion(n):
    """递归法计算斐波那契数列值，指数级r

    :param n: 第n个斐波那契数,n>=0
    :return:返回结果
    """
    if n > 2:
        return fibonaccin_recursion( n -1 ) +fibonaccin_recursion( n -2)
    elif n == 1 or n == 2:
        return 1
    else:
        return 0

def fibonaccin_dp(n):
    """动态规划计算斐波那契数列值，指数级r

    :param n: 第n个斐波那契数,n>=0
    :return:返回结果
    """
    result_record = [0, 1, 1]
    for i in range(2, n+ 1):
        result_record[i] = result_record[i - 1] + result_record[i - 2]
        result_record.append(result_record[i])
    return result_record[n]

start = time.clock()
print(fibonaccin_recursion(3))
end = time.clock()
print("递归法计算消耗时间是%0.2fs" %(end-start), end="\n\n")

start = time.clock()
print(fibonaccin_dp(10000))
end = time.clock()
print("动态规划计算消耗时间是%0.2fs" %(end-start))

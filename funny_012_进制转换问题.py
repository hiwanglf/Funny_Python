# Py从小喜欢奇特的东西，而且天生对数字特别敏感，一次偶然的机会，他发现了一个有趣的四位数2992，
# 这个数，它的十进制数表示，其四位数字之和为2+9+9+2=22，它的十六进制数BB0，其四位数字之和也为22，
# 同时它的十二进制数表示1894，其四位数字之和也为22，啊哈，真是巧啊。
# Py非常喜欢这种四位数，由于他的发现，所以这里我们命名其为Py数。
# 现在给你一个十进制4位数n，你来判断n是不是Py数，若是，则输出Yes，否则输出No。
# 如n=2992，则输出Yes； n = 9999，则输出No。

n = 2990

def num_to_list(n, method=12):
    """进制数字转换

    :param n:需要转化的十进制数字
    :param method:需要转换成几进制
    :return:返回一个列表
    """
    num_list = []
    while(n > 0):
        num_list.append(n%method)
        n = int(n/method)
    num_list.reverse()
    return sum(num_list)

if num_to_list(n,10) == num_to_list(n,12) and num_to_list(n,10) == num_to_list(n,16):
    print("Yes")
else:
    print("No")

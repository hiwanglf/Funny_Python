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



#
# 描述:
# 给你一个十进制数a，将它转换成b进制数,如果b>10,用大写字母表示（10用A表示，等等）
# a为32位整数，2 <= b <= 16
# 如a=3,b = 2, 则输出11

# 注意：需要处理负数！！！需要注意0
def num_to_list(n, method=12):
    """进制数字转换

    :param n:需要转化的十进制数字
    :param method:需要转换成几进制
    :return:返回一个列表
    """
    if n == 0:
        return [0]
    num_list = []
    while(n > 0):
        num_list.append(n%method)
        n = int(n/method)
    num_list.reverse()
    return num_list


def num_to_str(num_list):
    """数字列表转为字符列表

    :param num_list:整数列表
    :return:字符列表
    """
    str_list = []
    for num in num_list:
        str_list.append(str(num))
    return str_list

dict = {
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F'
}

a = -110
b = 2

# 符号判断，如果负数，将符号保留，正数则无符号
if a < 0:
    sign = "-"
    a = abs(a)
else:
    sign = ""

num_list = num_to_list(a, b)
str_list = num_to_str(num_list)
if b < 11:
    print(sign + "".join(str_list))
else:
    final_list = []
    for str_atom in str_list:
        if str_atom in dict:
            final_list.append(dict[str_atom])
        else:
            final_list.append(str_atom)
    print(sign + "".join(final_list))

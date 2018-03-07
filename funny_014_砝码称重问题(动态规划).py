# 描述:
# 有一组砝码，重量互不相等，分别为m1、m2、m3……mn；它们可取的最大数量分别为x1、x2、x3……xn。
# 现要用这些砝码去称物体的重量,问能称出多少种不同的重量。
# 现在给你两个正整数列表w和n， 列表w中的第i个元素w[i]表示第i个砝码的重量，列表n的第
# i个元素n[i]表示砝码i的最大数量。i从0开始，请你输出不同重量的种数。
# 如：w=[1,2], n=[2,1], 则输出5（分析：共有五种重量：0,1,2,3,4）



w=[1,2,3]                     # 表示重量
n=[2,1,1]                     # 表示数量


def every_weight(weight, number):
    """计算同个重量的砝码，所能称重的列表

    :param weight: 单个砝码的重量
    :param number: 砝码数量
    :return: 返回能产生多少种结果的称重结果列表
    """
    weight_list = []
    for i in range(0,number+1):
        weight_list.append(weight*i)
    return weight_list

weight_history = [0]                        # 记录所有产生过的重量
# 便利所有重量，同个重量的砝码可以产生的重量数目先计算出来
for i in range(0, len(w)):
    weight_list = every_weight(w[i], n[i])
    # 将weight值暂时赋给一个新的列表，因为weight将改变，造成死循环
    old_history = weight_history
    for x in range(0, len(old_history)):
        for y in range(0, len(weight_list)):
            # 如果历史列表中的砝码质量和新的砝码质量之和不在历史列表当中，则加入到历史列表当中去
            if (old_history[x]+weight_list[y]) not in old_history:
                weight_history.append(old_history[x]+weight_list[y])

print(len(weight_history))


# 描述:
# 有一组砝码，重量互不相等，分别为m1、m2、m3……mn；每种砝码的数量有无限个。
# 现要用这些砝码去称物体的重量,给你一个重量n,请你判断有给定的砝码能否称出重量n。
# 现在给你一个正整数列表w和一个正整数n，列表w中的第i个元素w[i]表示第i种砝码的重量，
# n表示要你判断的重量。如果给定砝码能称出重量n，输出Yes，否则输出No。
# 例如，w=[2,5,11], n=9,则输出Yes（取两个2，一个5）。
# 下面这个算法效率太低
w = [2, 5, 11]
n = 13


def every_weight(weight, number):
    """计算同个重量的砝码，所能称重的列表

    :param weight: 单个砝码的重量
    :param number: 砝码数量
    :return: 返回能产生多少种结果的称重结果列表
    """
    weight_list = []
    for i in range(0, number + 1):
        weight_list.append(weight * i)
    return weight_list


def num_weight(w, n):
    """计算每个砝码可能的最大数量

    :param w:砝码的质量列表
    :param n:要实现的质量
    :return:返回单个砝码最大数量的列表
    """
    num = []
    for per_num in w:
        num.append(int(n / per_num + 1))
    return num



num = num_weight(w, n)
weight_history = [0]  # 记录所有产生过的重量
# 便利所有重量，同个重量的砝码可以产生的重量数目先计算出来
for i in range(0, len(w)):
    weight_list = every_weight(w[i], num[i])
    # 将weight值暂时赋给一个新的列表，因为weight将改变，造成死循环
    old_history = weight_history
    for x in range(0, len(old_history)):
        for y in range(0, len(weight_list)):
            # 如果历史列表中的砝码质量和新的砝码质量之和不在历史列表当中，则加入到历史列表当中去
            if (old_history[x] + weight_list[y]) not in old_history:
                weight_history.append(old_history[x] + weight_list[y])

if n in weight_history:
    print("Yes")
else:
    print("No")

# 描述:
# 有一组砝码，重量互不相等，分别为m1、m2、m3……mn；每种砝码的数量有无限个。
# 现要用这些砝码去称物体的重量,给你一个重量n,请你判断有给定的砝码能否称出重量n。
# 现在给你一个正整数列表w和一个正整数n，列表w中的第i个元素w[i]表示第i种砝码的重量，
# n表示要你判断的重量。如果给定砝码能称出重量n，输出Yes，否则输出No。
# 例如，w=[2,5,11], n=9,则输出Yes（取两个2，一个5）。
# 高效率算法

def check_mod(new_list, n):
    """检查新产生的列表里面这些元素能不能凑成n

    :param new_list:整数列表
    :param n:要凑成的数
    :return:返回整数求余之后的数值
    """
    new_list.reverse()
    # for循环当中取余时候，必须从大的数字往小的数字走
    for weight in new_list:
        if n == 0:
            break
        if weight <= n:
            n = n % weight
    return n
# 对初始列表进行排序，从小到大
w.sort()
flag = 'No'
length = len(w)
for i in range(1, length+1):
    result = check_mod(w[0:i], n)
    if result == 0:
        flag = 'Yes'
        break

print(flag)

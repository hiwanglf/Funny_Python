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

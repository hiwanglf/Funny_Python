# 描述:
# 给你一个整数list L, 如 L=[2,-3,3,50], 求L的一个连续子序列，使其和最大，输出最大子序列的和。
# 例如，对于L=[2,-3,3,50]， 输出53（分析：很明显，该列表最大连续子序列为[3,50]).


L=[2,-3,3,50,-10,12]
count = []


def child_list(L):
    """求一个列表的所有有序子集合

    :param L:列表
    :return:返回新的包含有序子列表的列表
    """
    l = len(L)
    all_son_list = []
    for x in range(l):
        for y in range(x+1,l+1):
            all_son_list.append(L[x:y])

    return all_son_list


all = child_list(L)

for son in all:
    count.append(sum(son))

print(max(count))

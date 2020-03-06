# encoding=utf-8
# 冒泡排序算法的流程如下：
#
# 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
# 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
# 针对所有的元素重复以上的步骤，除了最后一个。
# 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
# 最差情况下的性能O（n ^ 2）
# 最佳案例表现O（n）
# 平均个案表现O（n ^ 2）


def bubble_sort(collection):
    """冒泡排序

    :param collection:传入要排序的列表
    :return:排序完成的列表
    """
    length = len(collection)
    for i in range(length-1):
        for j in range(length):
            if collection[j] > collection[i+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]
    return collection


#

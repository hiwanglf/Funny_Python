# 描述:
# 还记得中学时候学过的杨辉三角吗？具体的定义这里不再描述，你可以参考以下的图形：
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# ..............
# 先在给你一个正整数n，请你输出杨辉三角的前n层
# 注意：层数从1开始计数,每层数字之间用一个空格隔开，行尾不要有空格。
# 如n=2,则输出：
# 1
# 1 1

# 受限定义在初始的情况下，即一行的时候杨辉三角里面的内容
yanghui = [['1']]

# 因为第一行已经定义，所以循环条件设置为n>1
while(n > 1):
    new_line = ['1']                        # 定义新行的第一个元素为1；
    # 循环，从上一行获取下一行的元素值
    for i in range(0, len(yanghui[-1])-1):
        new_atom = str(int(yanghui[-1][i]) + int(yanghui[-1][i+1]))
        new_line.append(new_atom)
    new_line.append('1')                    # 定义新行的最后一个元素为1；
    yanghui.append(new_line)                # 将该行添加到杨辉三角列表集合当中
    n -= 1

for k in yanghui:
    print(" ".join(k))

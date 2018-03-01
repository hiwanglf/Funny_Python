# 描述:
# 下过象棋的人都知道，马只能走'日'字形（包括旋转90°的日），现在想象一下，给你一个n行m列网格棋盘，
# 棋盘的左下角有一匹马，请你计算至少需要几步可以将它移动到棋盘的右上角，若无法走到，则输出-1.
# 如n=1，m=2,则至少需要1步；若n=1，m=3,则输出-1。

#BFS算法
# 实现方法
# 1.首先将根节点放入队列中。
# 2.从队列中取出第一个节点，并检验它是否为目标。
#     ·如果找到目标，则结束搜寻并回传结果。
#     ·否则将它所有尚未检验过的直接子节点加入队列中。
# 3.若队列为空，表示整张图都检查过了——亦即图中没有欲搜寻的目标。结束搜寻并回传“找不到目标”。
# 4.重复步骤2。



m = 4
n = 2

step_postion = []               # 记录走过了哪些节点
start_position = [[0, 0]]       # 记录每一步的开始节点，初始是[[0,0]]
action = [[1, 2], [2, 1], [-1, -2], [-2, -1],[-1,2], [-2, 1], [1, -2], [2, -1]]

history = []                    # 用来存储上一次step_position里面的数据
t = 0                           # 记录步数

while(True):
    # 从每一个节点出发，然后遍历所有符合的节点
    for i in range(len(start_position)):
        for act in action:
            position = [start_position[i][0]+act[0], start_position[i][1]+act[1]]
            # 判断是否符合position的约束条件，如果符合并且position你没有在start表里面，则追加进去。
            if 0 <= position[0] <= m and 0 <= position[1] <= n:
                if position not in start_position:
                    start_position.append(position)
    t = t+1                     # 计步器+1
    # 判断是否找到
    if [m, n] in start_position:
        print(t)
        break
    # 如果两次遍历下来没有发现新节点，证明已经遍历了所有可以到达的节点，仍然没有发现所需要的，则未找见
    if history == start_position:
        print(-1)
        break
    else:
        history = []
        for po in start_position:
            history.append(po)

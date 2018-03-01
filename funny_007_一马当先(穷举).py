# 描述:
# 下过象棋的人都知道，马只能走'日'字形（包括旋转90°的日），现在想象一下，给你一个n行m列网格棋盘，
# 棋盘的左下角有一匹马，请你计算至少需要几步可以将它移动到棋盘的右上角，若无法走到，则输出-1.
# 如n=1，m=2,则至少需要1步；若n=1，m=3,则输出-1。


m = 4
n = 4

point_list = []         # 存储已经走过了哪些坐标点
step_dict={0:[(0,0)]}   # 存储第几步走过的点的列表，第几步，走过了哪些节点
i = 0                   # 用来记录步数
flag = True             # 标记，意味着程序继续while循环

while flag:
    # 从step_dict里面取出步数和即将走的点
    step_list = step_dict.get(i, [])
    i = i+1
    # print(step_list)
    # print(i)
    # 如果还有新点，则再次进入，继续探索
    if step_list:
        # 从已经走过的字典中取出上一步走过的点
        for point in step_list:
            #每个点都可以往8个方向走
            eight = ((point[0] - 1, point[1] - 2), (point[0] - 1, point[1] + 2),
                     (point[0] + 1, point[1] - 2), (point[0] + 1, point[1] + 2),
                     (point[0] - 2, point[1] - 1), (point[0] + 2, point[1] - 1),
                     (point[0] - 2, point[1] + 1), (point[0] + 2, point[1] +1))
            if (m, n) in eight:
                # 如果右上角的点在八个点当中，证明已经走到，即可以打印步数，退出程序
                print(i)
                flag = False
                break
            for per_eight in eight:
                if per_eight == (0, 0):
                    continue
                #elif per_eight not in step_list and per_eight[0] >= 0 and per_eight[0] <= m and per_eight[1] >= 0 and per_eight[1] <= n:
                elif per_eight not in step_list and 0 <= per_eight[0] <= m and 0 <= per_eight[1] <= n:
                    # 如果8个方向中的点不在已经走过的列表里面,则将新点加入到point_list当中；
                    point_list.append(per_eight)
                    # 如果8个方向中的点不在已经走过的列表里面，则将新点加入到step_dict里面，准备下一步在从这些点出发，去往下一个8点
                    step_dict.setdefault(i,[]).append(per_eight)
    # 如果已经没有新点，则证明无法到达右上角的点，退出
    else:
        print(-1)
        break

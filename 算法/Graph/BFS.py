# https://www.bilibili.com/video/av25763384/?spm_id_from=333.788.videocard.0

# 无序图
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['D', 'C'],
    'F': ['D']
}


class Solution:
    def BFS(self, graph, s):
        """

        :param graph: 图，字典形式输入
        :param s: 开始节点
        :return: 看具体情况
        """
        queue = [s]                 # use list for queue
        seen = set(s)                # set storage node had read
        parents = {                 # storage prefer node /parent node
            s: None
        }
        while len(queue) > 0:
            vertex = queue.pop(0)
            nodes = graph[vertex]
            for w in nodes:
                if w not in seen:
                    queue.append(w)
                    seen.add(w)
                    parents[w] = vertex
            print(vertex)           # print bfs read result
        return parents


test = Solution()
res = test.BFS(graph, 'A')
print(res)

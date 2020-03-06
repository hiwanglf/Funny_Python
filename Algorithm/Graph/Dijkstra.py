# https://www.bilibili.com/video/av25829980/?spm_id_from=333.788.videocard.0
import heapq
import math


graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'D': 3, 'C': 8},
    'F': {'D': 6}
}


def init_distance(graph, s):
    """
    init distance for s node to other node,set inf
    :param graph:
    :param s: start node
    :return:  distance dictionary
    """
    distance = {s: 0}
    for vertex in graph:
        if vertex is not s:
            distance[vertex] = math.inf
    return distance




def Dijkstra(graph, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    seen = set(s)
    parent = {
        s: None
    }
    distance = init_distance(graph, s)

    while len(pqueue) > 0:
        pair = heapq.heappop(pqueue)        # return tuple
        dist = pair[0]                      # distance
        vertex = pair[1]                    # node
        seen.add(vertex)                    # add pop node to seen set

        nodes = graph[vertex].keys()        # start to read every node neighbor to vertex
        for w in nodes:
            if w not in seen:               # if node not in seen
                if dist + graph[vertex][w] < distance[w]:   # if vertex to w and old distance smaller than pqueue history
                    heapq.heappush(pqueue, (dist + graph[vertex][w], w))    # push new distance to queue
                    parent[w] = vertex                                      # update w node's parent node
                    distance[w] = dist + graph[vertex][w]                   # update w node's distance to s node

    return parent, distance


p, d = Dijkstra(graph, 'A')
print(p)            # {'A': None, 'B': 'C', 'C': 'A', 'D': 'B', 'E': 'D', 'F': 'D'}
print(d)            # {'A': 0, 'B': 3, 'C': 1, 'D': 4, 'E': 7, 'F': 10}


# print A to D shortest path
def shortest_path(parent, dest):
    path = [dest]
    node = dest
    while parent[node]:
        path.append(parent[node])
        node = parent[node]
    path.reverse()      # reverse no return but modify himself
    return path


print(shortest_path(p, 'E'))

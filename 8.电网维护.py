'''
给你一个整数 c，表示 c 个电站，每个电站有一个唯一标识符 id，从 1 到 c 编号。

这些电站通过 n 条 双向 电缆互相连接，表示为一个二维数组 connections，其中每个元素 connections[i] = [ui, vi] 表示电站 ui 和电站 vi 之间的连接。直接或间接连接的电站组成了一个 电网 。

最初，所有 电站均处于在线（正常运行）状态。

另给你一个二维数组 queries，其中每个查询属于以下 两种类型之一 ：

[1, x]：请求对电站 x 进行维护检查。如果电站 x 在线，则它自行解决检查。如果电站 x 已离线，则检查由与 x 同一 电网 中 编号最小 的在线电站解决。如果该电网中 不存在 任何 在线 电站，则返回 -1。

[2, x]：电站 x 离线（即变为非运行状态）。

返回一个整数数组，表示按照查询中出现的顺序，所有类型为 [1, x] 的查询结果。

注意：电网的结构是固定的；离线（非运行）的节点仍然属于其所在的电网，且离线操作不会改变电网的连接性。
'''
import heapq
from collections import defaultdict
from typing import List


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        # 为每个连通分量维护一个最小堆，存储在线节点
        self.online_nodes = [list() for _ in range(n)]
        # 记录每个节点的在线状态
        self.online = [True] * n

        # 初始化，所有节点都在线
        for i in range(n):
            heapq.heappush(self.online_nodes[i], i)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return

        # 按秩合并
        #判断秩大小，较小的树合并到较大的树上
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
            # 合并在线节点堆，这里就是将小的堆的元素全部加入到大的堆中
            while self.online_nodes[xroot]:
                node = heapq.heappop(self.online_nodes[xroot])
                heapq.heappush(self.online_nodes[yroot], node)
        #这里就反过来
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
            while self.online_nodes[yroot]:
                node = heapq.heappop(self.online_nodes[yroot])
                heapq.heappush(self.online_nodes[xroot], node)
        #秩相等时，任选一棵树作为新的根，并将另一棵树合并到它上面，同时将新的根的秩加1
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1 #增加新根的秩（因为树的高度增加了）
            while self.online_nodes[yroot]:
                node = heapq.heappop(self.online_nodes[yroot])
                heapq.heappush(self.online_nodes[xroot], node)

    def set_offline(self, x):
        self.online[x] = False
        root = self.find(x)
        # 如果离线节点是堆顶，需要弹出直到找到在线节点
        while (self.online_nodes[root] and
               not self.online[self.online_nodes[root][0]]):
            heapq.heappop(self.online_nodes[root])

    def query(self, x):
        if self.online[x]:
            return x
        else:
            root = self.find(x)
            if not self.online_nodes[root]:
                return -1
            return self.online_nodes[root][0]


class Solution:
    def maintenanceCheck(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DSU(c + 1)  # 节点从1开始编号

        # 构建连通分量
        for u, v in connections:
            dsu.union(u, v)

        result = []
        for query in queries:
            if query[0] == 1:
                # 查询操作
                result.append(dsu.query(query[1]))
            else:
                # 离线操作
                dsu.set_offline(query[1])

        return result

if __name__ == "__main__":
    solution = Solution()
    c = 5
    connections = [[1,2],[2,3],[3,4],[4,5]]
    queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
    print(solution.maintenanceCheck(c, connections, queries))
    # 输出: [2, 1, 4, -1]
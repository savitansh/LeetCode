from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = self.createGraph(numCourses, prerequisites)
        vis = [0] * numCourses
        res = True
        for node in g:
            if vis[node] == 0:
                vis[node] = 1
                res = self.dfs(g, node, vis)
            if not res:
                return False
        return res

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = self.createGraph(numCourses, prerequisites)
        vis = [0] * numCourses
        ans = []
        for node in g:
            if vis[node] == 0:
                vis[node] = 1
                stk = []
                res = self.dfs(g, node, vis, stk)
                if res is False:
                    return []
                ans.extend(stk)
        return ans

    def dfs(self, graph, source, vis, stk):
        for nbr in graph[source]:
            if vis[nbr] == 1:
                return False
            if vis[nbr] == 0:
                vis[nbr] = 1
                res = self.dfs(graph, nbr, vis, stk)
                if not res:
                    return res
        vis[source] = 2
        stk.append(source)
        return True

    def createGraph(self, nodes, prerequisites):
        g = {}
        for n in range(nodes):
            g[n] = []
        for edge in prerequisites:
            g[edge[0]].append(edge[1])
        return g


if __name__ == '__main__':
    s = Solution()
    print(s.findOrder(7, [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]))

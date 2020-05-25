from typing import List


class Solution:
    def numIslands(self, g: List[List[str]]) -> int:
        n = len(g)
        m = len(g[0])
        color = 1
        grid = []
        for i in range(n):
            r = [0] * m
            grid.append(r)
        for i in range(n):
            for j in range(m):
                grid[i][j] = int(g[i][j])
        atleastOneExits = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    color += 1
                    grid[i][j] = color
                    atleastOneExits = True
                    self.dfs(grid, i, j, color, n, m)
        return color - 1 if atleastOneExits else 0

    def dfs(self, grid, i, j, color, n, m):
        if i >= 1 and grid[i - 1][j] == 1:
            grid[i - 1][j] = color
            self.dfs(grid, i - 1, j, color, n, m)
        if j >= 1 and grid[i][j - 1] == 1:
            grid[i][j - 1] = color
            self.dfs(grid, i, j - 1, color, n, m)
        if i + 1 < n and grid[i + 1][j] == 1:
            grid[i + 1][j] = color
            self.dfs(grid, i + 1, j, color, n, m)
        if j + 1 < m and grid[i][j + 1] == 1:
            grid[i][j + 1] = color
            self.dfs(grid, i, j + 1, color, n, m)


if __name__ == '__main__':
    s = Solution()
    print(s.numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    ))

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0:
            return
        m = len(board[0])
        for i in range(m):
            self.traverse(board, 0, i, n, m)
            self.traverse(board, n - 1, i, n, m)
        for i in range(n):
            self.traverse(board, i, 0, n, m)
            self.traverse(board, i, m - 1, n, m)
        for i in range(n):
            for j in range(m):
                board[i][j] = 'X' if board[i][j] == 'O' else board[i][j]
        for i in range(n):
            for j in range(m):
                board[i][j] = 'O' if board[i][j] == '_' else board[i][j]

    def traverse(self, board, i, j, n, m):
        if i < 0 or j < 0 or i >= n or j >= m:
            return
        if board[i][j] == 'X':
            return
        board[i][j] = '_' if board[i][j] == 'O' else board[i][j]
        if i >= 1 and board[i - 1][j] == 'O':
            self.traverse(board, i - 1, j, n, m)
        if i + 1 < n and board[i + 1][j] == 'O':
            self.traverse(board, i + 1, j, n, m)
        if j >= 1 and board[i][j - 1] == 'O':
            self.traverse(board, i, j - 1, n, m)
        if j + 1 < m and board[i][j + 1] == 'O':
            self.traverse(board, i, j + 1, n, m)


if __name__ == '__main__':
    s = Solution()
    board = [["X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X"], ["X", "O", "X", "O", "X", "O"],
             ["O", "X", "O", "X", "O", "X"]]
    # board = [['O', 'O']]
    s.solve(board)
    print(board)

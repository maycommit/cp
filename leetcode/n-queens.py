from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def make_board(n):
            return [['.' for _ in range(n)] for _ in range(n)]

        def is_valid(board, row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1


            i, j = row, col
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def solve(board, row, solutions):
            if row == n:
                solutions.append([ "".join(x) for x in board])
                return

            for i in range(len(board)):
                if is_valid(board, row, i):
                    board[row][i] = 'Q'
                    solve(board, row + 1, solutions)
                    board[row][i] = '.'


        solutions = []
        solve(make_board(n), 0, solutions)

        return solutions


s = Solution()
print(s.solveNQueens(4))
print(s.solveNQueens(1))


from collections import defaultdict
import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [[False]*9 for _ in range(9)]
        col = [[False]*9 for _ in range(9)]
        box = [[False]*9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    digit = int(board[i][j])
                    idx = (i // 3) * 3 + (j // 3)

                    if row[i][digit-1] or col[j][digit-1] or box[idx][digit-1]:
                        return False

                    row[i][digit-1] = True
                    col[j][digit-1] = True
                    box[idx][digit-1] = True

        return True


# better:


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

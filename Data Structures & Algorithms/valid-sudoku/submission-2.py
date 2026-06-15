class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # HASH SET | O(n^2), O(n^2)
        # check entire board in one pass
        rows = defaultdict(set)         # keep digits in row r
        cols = defaultdict(set)         # keep digits in col c
        squares = defaultdict(set)      # keep digits in 3x3 box

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r]:
                    return False
                if board[r][c] in cols[c]:
                    return False
                if board[r][c] in squares[(r // 3, c // 3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True

        # BRUTE FORCE | time: O(n^2), space: O(n)
        # check row is correct
        for row in range(9):
            seen = set()
            for c in range(9):
                if board[row][c] == ".":
                    continue
                if board[row][c] in seen:
                    return False
                seen.add(board[row][c])

        # check column is correct
        for col in range(9):
            seen = set()
            for r in range(9):
                if board[r][col] == ".":
                    continue
                if board[r][col] in seen:
                    return False
                seen.add(board[r][col])

        # check square
        for square in range(9):
            seen = set()
            for r in range(3):
                for c in range(3):
                    row = (square // 3) * 3 + r
                    col = (square % 3) * 3 + c
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True
        
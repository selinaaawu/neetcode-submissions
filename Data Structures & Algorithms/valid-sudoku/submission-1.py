class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check horizontal
        for row in range(9):
            row_set = set()
            for i in range(9):
                s = board[row][i]
                if s != "." and s in row_set:
                    return False
                row_set.add(s)
        
        # check vertical
        for col in range(9):
            column_set = set()
            for i in range(9):
                s = board[i][col]
                if s != "." and s in column_set:
                    return False
                column_set.add(s)

        # check 3x3 squares
        for square in range(9):
            square_set = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j

                    s = board[row][col]
                    if s != "." and s in square_set:
                        return False
                    square_set.add(s)

        return True
                
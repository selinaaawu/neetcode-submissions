class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ## BINARY SEARCH | time: O(log(m*n)), space: O(1)
        # flatten matrix into sorted array, binary search 0 to rows*cols-1
        # map m to matrix w row = m //cols, col = m % cols
        # l = 0, r = 11, m = 5, arr[m] = 11
        # 4 = row 1, column 0
        # 5 = row 1, column 1
        # 6 = row 1, column 2
        # 7 = row 1, column 3
        # 8 = row 2, column 0
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows * cols - 1
        while l <= r:
            mid = l + (r - l) // 2
            row, col = mid // cols, mid % cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

        
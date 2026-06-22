class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ## BINARY SEARCH
        # l = 0, r = 11, m = 5, arr[m] = 11
        # 4 = row 1, column 0
        # 5 = row 1, column 1
        # 6 = row 1, column 2
        # 7 = row 1, column 3
        # 8 = row 2, column 0
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows * cols - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid // cols][mid % cols] == target:
                return True
            elif matrix[mid // cols][mid % cols] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

        
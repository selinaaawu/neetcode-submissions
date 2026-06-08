class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row * col - 1
        while left <= right:
            mid = left + ((right - left) // 2)  # mid = 5
            r, c = mid // col, mid % col        # r = 1 c = 1
            if matrix[r][c] > target:
                right = mid - 1
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                return True

        return False
        

        # ## BRUTE FORCE | O(nm)
        # for row in matrix:
        #     for element in row:
        #         if element == target:
        #             return True
        # return False
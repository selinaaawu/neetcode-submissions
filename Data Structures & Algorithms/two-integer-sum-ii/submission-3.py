class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] == target - numbers[right]:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                # 1 + 4 = 5 > 3
                right -= 1
            else:
                # 1 + 4 = 5 < 6
                left += 1
        return false





































        lPointer, rPointer = 0, len(numbers) - 1
        while lPointer < rPointer:
            sum = numbers[lPointer] + numbers[rPointer]
            if sum == target:
                return [lPointer + 1, rPointer + 1]
            elif sum > target:
                rPointer -= 1
            else:
                lPointer += 1
            
        return []
        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # TWO POINTER |  
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                # increment for 1-indexed array
                return [left + 1, right + 1]
        return False
        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lPointer, rPointer = 0, len(numbers) - 1
        while lPointer < rPointer:
            sum = numbers[lPointer] + numbers[rPointer]
            if sum == target:
                break
            elif sum > target:
                rPointer -= 1
            else:
                lPointer += 1
            
        return [lPointer + 1, rPointer + 1]
        
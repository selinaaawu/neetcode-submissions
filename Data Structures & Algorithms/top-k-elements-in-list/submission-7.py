class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # BUCKET SORT | time: O(n), space: O(n)
        # frequency map of {num : frequency}
        numMap = defaultdict(int)
        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)

        # list of frequency[i] = num that appear i times
        frequency = [[] for i in range(len(nums) + 1)]
        for num, count in numMap.items():
            frequency[count].append(num)

        # loop from largest frequency, adding num in freq[i] to result
        # return result once k numbers
        result = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result

        # SORTING | time: O(n log n), space: O(n)
        # hash map of {num : frequency}
        numMap = defaultdict(int)
        for num in nums:
            numMap[num] += 1

        # list of [frequency, num] and sort by frequency
        newMap = []
        for key, value in numMap.items():
            newMap.append((value, key))
        newMap.sort()

        # pop num from back and add to result until k elements added
        result = []
        while len(result) < k:
            result.append(newMap.pop()[1])
        return result

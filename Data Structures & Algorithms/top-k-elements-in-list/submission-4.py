class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # BUCKET SORT | O(n)
        # # mapping number to its occurence
        # mapping = {}
        # for num in nums:
        #     mapping[num] = 1 + mapping.get(num, 0)
        
        # # bucket sort number
        # # [ 0  ... len(nums) ]      frequency
        # # [ [] ... []        ]      num
        # freq = [[] for i in range(len(nums) + 1)]
        # for num, count in mapping.items():
        #     freq[count].append(num)
        
        # # find k most frequent
        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res



        # # MIN HEAP | O(nlogk)
        # # mapping number to its occurence
        # mapping = {}        # [num : frequency]
        # for num in nums:
        #     mapping[num] = 1 + mapping.get(num, 0)
        
        # # push [frequency, num] and pop least frequent
        # heap = []           # (frequency, num)
        # for num in mapping.keys():
        #     heapq.heappush(heap, (mapping[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # # pop least frequent and retrieves num
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res



        # SORTING W HASHMAP | O(nlogn)
        # mapping number to its occurence
        mapping = {}        # [num : frequency]
        for num in nums:
            mapping[num] = 1 + mapping.get(num, 0)

        # reversing and sorting by frequency
        arr = []            # [frequency, num]
        for num, count in mapping.items():
            arr.append([count, num])
        arr.sort()

        # finding k most frequent
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

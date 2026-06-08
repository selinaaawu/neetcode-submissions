class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:































        # BUCKET SORT | O(n)
        # mapping number to its occurence
        mapping = Counter(nums)
        
        # bucket sort number
        # [ 0  ... len(nums) ]      frequency
        # [ [] ... []        ]      num
        freq = [[] for i in range(len(nums) + 1)]
        for num, count in mapping.items():
            freq[count].append(num)
        
        # find k most frequent
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


        # MIN HEAP | O(nlogk)
        # mapping number to its occurence
        mapping = Counter(nums)
        
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

        # push [frequency, num] and pop least frequent
        heap = []
        for num, freq in hashMap.items():
            heapq.heappush(heap, (freq, num))
            if (len(heap)) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]



        # SORTING W HASHMAP | O(nlogn)
        # mapping number to its occurence
        mapping = Counter(nums)

        # # reversing and sorting by frequency
        # arr = []            # [frequency, num]
        # for num, count in mapping.items():
        #     arr.append([count, num])
        # arr.sort()

        # # finding k most frequent
        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res
        
        # sort by frequency
        arr = list(dict(sorted(hashMap.items(), key=lambda x : x[1], reverse=True)))
        
        # return k most frequent
        return arr[:k]
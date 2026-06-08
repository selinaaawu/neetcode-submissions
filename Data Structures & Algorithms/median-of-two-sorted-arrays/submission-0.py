class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ## BINARY SEARCH
        # array A = smaller array
        A, B = nums1, nums2
        if len(nums1) > len(nums2):         # A = [3], B = [1,2]
            A, B = nums2, nums1
        total = len(A) + len(B)
        half = total // 2
        
        left, right = 0, len(A) - 1
        while True:
            midA = left + (right - left) // 2
            midB = half - midA - 2

            aLeft = A[midA] if midA >= 0 else float('-inf')
            aRight = A[midA + 1] if (midA + 1) < len(A) else float('inf')
            bLeft = B[midB] if midB >= 0 else float('-inf')
            bRight = B[midB + 1] if (midB + 1) < len(B) else float('inf')

            if aLeft <= bRight and bLeft <= aRight:
                # even
                if total % 2 == 0:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
                else:
                    return min(aRight, bRight)
                # odd
            elif aLeft > bRight:
                right = midA - 1
            else:
                left = midA + 1



        ## IDK WHAT THIS IS
        pointer1, pointer2 = 0, 0
        size = len(nums1) + len(nums2)        # 3
        medianI = size // 2                 # 1
        # odd

        while (pointer1 + pointer2) < medianI:
            if nums1[pointer1] <= nums2[pointer2]:
                pointer1 += 1
            else:
                pointer2 += 1
        
        median = nums1[pointer1]
        if nums1[pointer1] > nums2[pointer2]:
            median = nums2[pointer2]
        
        return median
        
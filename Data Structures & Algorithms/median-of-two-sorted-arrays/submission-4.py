class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find total length for both lists
        # if odd -> find mid value
        # if even -> find 2 mid value / 2

        # two pointers, both at beginning of each
        # move smaller pointer until get to mid length

        ## TWO POINTERS
        len1, len2 = len(nums1), len(nums2)
        i = j = 0
        median1 = median2 = 0

        for count in range((len1 + len2) // 2 + 1):
            median2 = median1

            # while both pointers have more to traverse
            if i < len1 and j < len2:
                if nums1[i] <= nums2[j]:
                    median1 = nums1[i]
                    i += 1
                else:
                    median1 = nums2[j]
                    j += 1
            # nums2 at end
            elif i < len1:
                median1 = nums1[i]
                i += 1
            # nums1 at end
            else:
                median1 = nums2[j]
                j += 1
        
        # if evan -> return average of two median values
        if (len1 + len2) % 2 == 0:
            return (median1 + median2) / 2.0
        # if odd -> return median
        else:
            return float(median1)
        
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if two strings contain same # of characters



        # hash set | 

        # hash map | map occurence of letter to num, check for equality
        # time: O(n + m), space: O(1)
        if len(s) != len(t): 
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

        # sort | sort string and compare
        # O(nlogn + mlogm), space: O( + m)
        return sorted(s) == sorted(t)


        
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # TWO POINTER | time: O(n), space: O(1)
        left, right = 0, len(s) - 1

        while left < right:
            # skip characters that are not letters or digits (alnum)
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # compare lowercase characters (ignores case)
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        
        return True
        
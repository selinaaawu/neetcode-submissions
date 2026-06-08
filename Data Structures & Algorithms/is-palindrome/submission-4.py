class Solution:
    def isPalindrome(self, s: str) -> bool:
        # start
        # return s == s[::-1]

        print(s)
        



































        
        ## TWO POINTERS
        # l at front, r at back
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

        # # REVERSE STRING
        # clean_str = ""
        # for char in s:
        #     if char.isalnum():
        #         clean_str += char.lower()
        # return clean_str == clean_str[::-1]




        
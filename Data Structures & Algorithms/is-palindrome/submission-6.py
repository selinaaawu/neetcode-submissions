class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using two pointers
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and s[l].isalnum() == False:
                l += 1
            while l < r and s[r].isalnum() == False:
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True
        
        # using reverse string
        clean = ""
        for char in s:
            if char.isalnum():
                clean += char.lower()
        print(clean)
        print(clean[::-1])

        return clean == clean[::-1]
        



































        
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




        
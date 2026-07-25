class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create 2 pointers, one at the start/left (index 0)
        # 2nd pointer called right/r at the end of string (index length of string - 1)
        l, r = 0, len(s) - 1

        # create a while loop to make sure that the left pointer never passes right pointer
        while l < r:
            # creat a new while loop where we check if the char is alphanumeric
            # if character is not alphanumeric, we keep increasing the index until it is
            # we do this for both pointers, but decrease for right
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            
            # increment left and decrement right after checking if both pointers are the same characters
            l += 1
            r -= 1
        
        return True
        
    # in case I can't use the .isalnum method, create my own where I check if 
    # the character is alphanumeric
    def isAlphaNum(self, c):
        return ("a" <= c.lower() <= "z" or "0" <= c.lower() <= "9")
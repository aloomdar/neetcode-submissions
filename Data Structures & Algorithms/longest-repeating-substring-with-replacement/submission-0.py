class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # create a hashmap to count the occurence of each character
        count = {}
        res = 0

        l = 0 
        for r in range(len(s)):
            # increment the number of occurences of the letter in the string 
            count[s[r]] = 1 + count.get(s[r], 0)
            # create a while loop to check if the number of replacements in the window
            # is greater than the number of letters we can change
            # if it is greater, then we shift the left pointer after decrementing the count 
            # of the letter at the left pointer
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            # 
            res = max(res, r - l + 1)
        return res
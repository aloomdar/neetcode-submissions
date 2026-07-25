class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create an empty character set
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # if the letter at s[r] is in the character set
            # we keep adding 1 to the left pointer until s[r] is no longer in the set
            # charSet.remove only happens if we see the character s[r] at s[l]
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # we add s[r] back to the character set 
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
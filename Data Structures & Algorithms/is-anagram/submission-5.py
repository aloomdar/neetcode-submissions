class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charCount = {}
        charCount2 = {}
        for i in range(len(s)):
            charCount[s[i]] = 1 + charCount.get(s[i], 0)
            charCount2[t[i]] = 1 + charCount2.get(t[i], 0)

        return charCount == charCount2
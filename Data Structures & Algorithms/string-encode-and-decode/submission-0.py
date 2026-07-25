class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # result is going to be the length of the string plus a delimiter
            # plus the string itself 
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # res is a list, i is the starting point of the string
        res, i = [], 0

        while i < len(s):
            j = i
            #increment j until we find the delimiter I decided on
            while s[j] != "#":
                j += 1
            # I find the length of the word by slicing the list until the delimiter
            length = int(s[i:j])
            # I am appending to the list the word by incrementing j + 1
            # j + 1 is the start of the word
            # j + 1 + length is the end of the word
            res.append(s[j + 1: j + 1 + length])
            # i is going to start at the end of the previous word
            i = j + 1 + length
        return res


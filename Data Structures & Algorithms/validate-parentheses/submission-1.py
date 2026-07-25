class Solution:
    def isValid(self, s: str) -> bool:

        # create a hash map of characters, closing corresponds to opening
        # im doing closing to opening instead of open to close
        # because when I push to the stack, It should be opening 
        # and when i run into a closing, i'm going to check if 
        # the opening is in the stack and if it is, i'm not going to push  but pop
        chars = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        stack = []

        # i am checking the character in string s
        for c in s:
            # this runs if the character is a closing
            if c in chars:
                # i am checking if the stack exists
                # if the stack exists, then I check if the last 
                # element in the stack, or the more recently added
                # is the corresponding open to the closing char that we see in string s
                # if it is, then we pop the most recently added element
                if stack and stack[-1] == chars[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        if stack:
            return False
        return True


        
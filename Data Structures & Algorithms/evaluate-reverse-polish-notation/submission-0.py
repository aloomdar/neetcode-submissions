class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                # I cast to int because it will round the number down to closer to 0 
                # so if I have 1.7 as the result of division, it will round to 1 
                # or if it's -1.5, it will round to -1 instead of -2
                stack.append(int(b / a))
            else:
                # cast to int because all the tokens are strings
                stack.append(int(token))
        return int(stack[0])
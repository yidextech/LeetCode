class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        i =0
        stack = []
        for i in range(len(tokens)):

            #check for opperations
            if tokens[i] == "+":
                result = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tokens[i] == "-":
                result = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tokens[i] == "*":
                result = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tokens[i] == "/":
                result = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(int(tokens[i]))
        return stack[0]
        
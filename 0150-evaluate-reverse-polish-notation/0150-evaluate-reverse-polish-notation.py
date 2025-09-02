class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        opp = {
            '+':operator.add,
            '-':operator.sub,
            '*':operator.mul,
            '/':operator.truediv
        }

        stack = []

        for token in tokens:
            if token in opp:
                b = stack.pop()
                a = stack.pop()
                ans = opp[token](a, b)
                stack.append(int(ans))
            else:
                stack.append(int(token))
        return stack[0]
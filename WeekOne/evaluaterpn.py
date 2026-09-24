class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        ops = "+-*/"

        for t in tokens:
            if  t not in ops:
                stack.append(int(t))
                continue
            
            if t == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n1 + n2))
            elif t == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2 - n1))
            elif (t == '*'):
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n1 * n2))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2/n1))
            
        return stack[-1]
                

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op1=0
        op2=0
        while(tokens):
            val=tokens.pop(0)
            if val not in "+-*/":
                stack.append(val)
            else:
                op2=int(stack.pop())
                op1=int(stack.pop())
                if val=='+':
                    stack.append(op1+op2)
                elif val=='-':
                    stack.append(op1-op2)
                elif val=='*':
                    stack.append(op1*op2)
                else:
                    stack.append(op1/op2)
        result=stack.pop()
        print(result)
        return int(result)
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open='({['
        close=')}]'
        for i in s:
            # print(stack)
            if i in open:
                stack.append(i)
            elif i in close and len(stack)>0:
                if i==')' and stack[-1]=='(' or i==']' and stack[-1]=='[' or i=='}' and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack)==0:
            return True
        return False
            
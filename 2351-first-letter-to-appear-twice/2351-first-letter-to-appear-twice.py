class Solution:
    def repeatedCharacter(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s.count(s[i])>1 and s[i] not in stack:
                stack.append(s[i])
            elif s.count(s[i])>1 and s[i] in stack:
                return s[i]
        return ''
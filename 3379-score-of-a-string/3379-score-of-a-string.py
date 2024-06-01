class Solution:
    def scoreOfString(self, s: str) -> int:
        s1=0
        for i in range(len(s)-1):
            # print(ascii(s[i]))
            s1=s1+abs(ord(s[i])-ord(s[i+1]))
        print(s1)
        return s1
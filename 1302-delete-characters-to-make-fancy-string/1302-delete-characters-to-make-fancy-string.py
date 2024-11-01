class Solution:
    def makeFancyString(self, s: str) -> str:
        str1=""
        prev=""
        for ele in s:
            if len(str1)>=2 and str1[-1]==ele and str1[-2]==ele:                    
                pass
            else:
                str1+=ele
        return str1
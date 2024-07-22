class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        l1=len(s1)
        s1=sorted(s1)
        left=0
        for r in range(len(s2)):
            while((r-left+1)>l1):
                left+=1
            dummy=sorted(s2[left:r+1])
            if dummy==s1:
                return True
        return False
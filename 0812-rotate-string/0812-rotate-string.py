class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i=0
        l=len(s)
        while(i<l):
            if(s==goal):
                return True
            s=s[1:]+s[0]
            i+=1
        return False
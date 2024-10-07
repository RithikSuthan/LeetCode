class Solution:
    def minLength(self, s: str) -> int:
        while(s.count("AB")!=0 or s.count("CD")!=0):
            if "AB" in s:
                ind=s.index("AB")
                temp=list(s)
                temp[ind]="_"
                temp[ind+1]="_"
                while "_" in temp:
                    temp.remove("_")
                s="".join(temp)
            if "CD" in s:
                ind=s.index("CD")
                temp=list(s)
                temp[ind]="_"
                temp[ind+1]="_"
                while "_" in temp:
                    temp.remove("_")
                s="".join(temp)
            # print(s)
        return len(s)
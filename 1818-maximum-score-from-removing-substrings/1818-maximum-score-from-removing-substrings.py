class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removeChar(s,pattern,point):
            # print("start",s)
            score=0
            st=[]
            for i in s:
                if st and (st[-1]+i==pattern):
                    score+=point
                    st.pop()
                else:
                    st.append(i)
            # print(st,score)
            return "".join(st),score
        score1,score2=0,0
        if x>y:
            s,score1=removeChar(s,"ab",x)
            s,score2=removeChar(s,"ba",y)
        else:
            s,score1=removeChar(s,"ba",y)
            s,score2=removeChar(s,"ab",x)
        
        return score1+score2

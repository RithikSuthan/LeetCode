class Solution:
    import math
    def minSwaps(self, s: str) -> int:
        st=[]
        unbalancedCount=0
        for ele in s:
            if ele=="[":
                st.append(ele)
            elif ele=="]" and not st:
                unbalancedCount+=1
            elif ele=="]" and st[-1]=="[":
                st.pop()
        return math.ceil(unbalancedCount/2)
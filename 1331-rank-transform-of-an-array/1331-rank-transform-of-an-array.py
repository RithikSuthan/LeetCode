class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        st=list(set(arr))
        st.sort()
        dict1={}
        rank=1
        for i in st:
            dict1[i]=rank
            rank=rank+1
        return [dict1[i] for i in arr]
        
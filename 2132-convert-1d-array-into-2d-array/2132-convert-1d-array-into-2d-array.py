class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        elements=m*n
        results=[]
        if elements==len(original):
            m=0
            k=n
            while(k<=len(original)):
                ls=original[m:k]
                m=m+n
                k=k+n
                results.append(ls)
            return results

        return []
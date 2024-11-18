class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans=[]
        for i in range ( len(code) ):
            temp=0
            if k>=0:
                for j in range(k):
                    # print(i+j+1)
                    temp += code[ (i+j+1) %len(code)]
            else:
                for j in range(1,-k+1):
                    temp += code[ (i-j) %len(code)]
            ans.append(temp)
            # print()
        return ans  
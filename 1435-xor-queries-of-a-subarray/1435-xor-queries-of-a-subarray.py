class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        temp=[0 for i in range(len(arr)+1)]
        for i in range(1,len(arr)+1):
            temp[i]=temp[i-1]^arr[i-1]
        # print(temp)
        
        ans=[]

        for query in queries:
            ans.append(temp[query[0]] ^ temp[query[1]+1])
        return ans
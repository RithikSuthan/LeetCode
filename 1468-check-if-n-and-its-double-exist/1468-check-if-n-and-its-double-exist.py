class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(0,len(arr)):
            if 2*arr[i] in arr: 
                if (arr[i]==0 and arr.count(0)==1):
                    pass
                else:
                    return True
        return False
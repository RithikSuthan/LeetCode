class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result=[]
        while(arr2):
            val=arr2.pop(0)
            while(val in arr1):
                arr1.remove(val)
                result.append(val)
        if (arr1):
            arr1.sort(key=lambda x:x)
            result.extend(arr1)
        return result
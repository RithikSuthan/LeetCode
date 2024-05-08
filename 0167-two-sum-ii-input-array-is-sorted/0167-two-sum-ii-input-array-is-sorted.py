class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1={}
        for i in range(len(numbers)):
            diff=target-numbers[i]
            
            if diff in dict1:
                return [dict1[diff]+1,i+1]
            if diff not in dict1:
                dict1[numbers[i]]=i
            print(dict1)
        return []
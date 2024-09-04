class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        # print(salary)
        if len(salary)<2:
            return 0
        result=salary[1:len(salary)-1]
        # print(result)
        return sum(result)/len(result)
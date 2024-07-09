class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t=customers[0][0]
        wait=[]
        for i in range(len(customers)):
            if customers[i][0]<=t:
                t+=customers[i][1]
            else:
                t=customers[i][0]+customers[i][1]
            wait.append(t-customers[i][0])
        return sum(wait)/len(customers)
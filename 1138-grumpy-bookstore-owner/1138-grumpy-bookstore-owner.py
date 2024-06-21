class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_satified=0
        already_satisfied=0
        grump=[]
        for i in range(len(grumpy)):
            if grumpy[i]!=1:
                already_satisfied+=customers[i]
            else:
                grump.append(i)
        max_satisfied=already_satisfied
        grump.sort()
        # print("line",max_satisfied,already_satisfied)
        # print("grump",grump)
        for i in range(len(customers)-minutes+1):
            start=i
            end=start+minutes-1
            # print(customers[start:end],start,end)
            temp=0
            for ind in grump:
                if ind>=start and ind<=end:
                    temp+=customers[ind]
                elif ind>end:
                    break
            max_satisfied=max(max_satisfied,temp+already_satisfied)

        return max_satisfied
        
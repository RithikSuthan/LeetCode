class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        ls=[0,0,0]
        for i in bills:
            print("Amount ",i)
            if i==5:
                ls[0]+=1
            elif i==10 and ls[0]>=1:
                ls[0]-=1
                ls[1]+=1
            elif i==20 and ls[1]>=1 and ls[0]>=1:
                ls[2]+=1
                ls[1]-=1
                ls[0]-=1
            elif i==20 and ls[1]<=0 and ls[0]>=3:
                ls[2]+=1
                ls[0]-=3
            else:
                return False
            # print(ls)
        return True
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num1=list(bin(start))
        num2=list(bin(goal))

        num1.pop(0)
        num1.pop(0)
        num2.pop(0)
        num2.pop(0)
        while len(num1)<len(num2):
            num1.insert(0,0)
        while len(num2)<len(num1):
            num2.insert(0,0)
        min1=0
        print(num1,num2)
        for i in range(len(num1)):
            if int(num1[i])!=int(num2[i]):
                min1+=1
        return min1
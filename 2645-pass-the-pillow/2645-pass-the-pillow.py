class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        flag=False
        cou=1
        ls=[i for i in range(1,n+1)]
        while(time>0):
            print("Enterred front")

            while(not flag):
                print(ls[cou-1],time)
                cou+=1
                time-=1
                if (cou==n):
                    flag=True
                if time==0:
                    return cou

            print("Enterred back")

            while(flag):
                print(ls[cou-1],time)
                cou-=1
                time-=1
                if (cou==1):
                    flag=False
                if time==0:
                    # print("Answer",cou)
                    return cou
        return -1
                
class Solution:
    def minimumSteps(self, s: str) -> int:
        # steps=0
        # temp=[]
        # for i in range(0,s.count("0")):
        #     temp.append("0")
        # for i in range(0,s.count("1")):
        #     temp.append("1")
        # arr=list(s)
        # while(arr!=temp):
        #     i=0
        #     while(i<len(s)-1):
        #         j=i+1
        #         if (arr[i]=="1" and arr[j]=="0"):
        #             arr[j],arr[i]=arr[i],arr[j]
        #             steps+=1
        #         i+=1
        # return steps

        black=0
        swaps=0
        for ele in s:
            if ele=="0":
                swaps+=black
            else:
                black+=1
        return swaps

        

    
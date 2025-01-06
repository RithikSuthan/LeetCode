class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] *len(boxes)
        print(ans)
        for i in range(0,len(boxes)):
            for j in range(0,i):
                if (boxes[j]=="1"):
                    ans[i]+=i-j
            for k in range(i+1,len(boxes)):
                if(boxes[k] == "1"):
                    ans[i] +=k-i
            # print(ans)
        return ans
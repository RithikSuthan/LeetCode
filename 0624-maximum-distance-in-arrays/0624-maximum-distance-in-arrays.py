class Solution(object):
    def maxDistance(self, arrays):
        min1=max(arrays[0])
        min_ind=None
        for i in range(len(arrays)):
            if min1>min(arrays[i]):
                min1=min(arrays[i])
                min_ind=i
        max_ind=0
        max1=min(arrays[0])
        for i in range(len(arrays)):
            if max1<max(arrays[i]) and min_ind!=i:
                max1=max(arrays[i])
                max_ind=i
        
        max2=min(arrays[0])
        max_ind2=0
        for i in range(len(arrays)):
            if max2<max(arrays[i]):
                max2=max(arrays[i])
                max_ind2=i
        min_ind2=0
        min2=max(arrays[0])
        for i in range(len(arrays)):
            if min2>min(arrays[i]) and max_ind2!=i:
                min2=min(arrays[i])
                min_ind2=i
        print(min1," ",max1)
        print(min2," ",max2)
        ans=max(abs(max1-min1),abs(max2-min2))
        return ans
        
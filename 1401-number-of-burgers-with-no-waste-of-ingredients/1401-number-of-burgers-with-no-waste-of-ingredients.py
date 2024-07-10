class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        low=0
        high=cheeseSlices
        while(low<=high):
            mid=(low+high)//2
            small=cheeseSlices-mid
            temp=4*mid+2*(cheeseSlices-mid)
            # print([mid,cheeseSlices],"temp=",temp)
            if (temp==tomatoSlices):
                return [mid,cheeseSlices-mid]
            elif temp>tomatoSlices:
                high=mid-1
            else:
                low=mid+1
        return []
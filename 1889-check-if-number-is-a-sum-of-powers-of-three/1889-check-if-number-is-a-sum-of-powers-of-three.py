import bisect
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        arr = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721]
        while(n > 0):
            # print(n, " ",arr)
            val = bisect.bisect_right(arr,n) - 1
            n -= arr[val]
            arr.pop(val)
            if n==0:
                return True
        return False

        


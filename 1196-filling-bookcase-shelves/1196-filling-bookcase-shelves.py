class Solution:
    from collections import defaultdict
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        memo=defaultdict(int)
        def helperfunc(i):
            if i==len(books):
                return 0
            nonlocal memo
            if i in memo:
                return memo[i]
            curr_width=shelfWidth
            max_h=0
            memo[i]=float("inf")
            # print("Call for ",i,memo)
            for j in range(i,len(books)):
                width,height=books[j][0],books[j][1]
                if curr_width<width:
                    break
                curr_width-=width
                max_h=max(max_h,height)
                memo[i]=min(  #better to add at same shelf or at new shelf
                    memo[i],max_h+helperfunc(j+1)
                )
                # print(memo)
            return memo[i]
        helperfunc(0)
        # print(memo)
        return memo[0]
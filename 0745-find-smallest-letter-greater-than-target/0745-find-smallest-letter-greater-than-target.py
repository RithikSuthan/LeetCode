class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        val=[ord(i) for i in letters]
        left,right=0,len(letters)
        print(val)
        while left<right:
            mid=(left+right)//2
            if val[mid]<=ord(target):
                left=mid+1
            else:
                right=mid
        print(left,mid,right)
        if right<len(val) and chr(val[right]) in letters:
            return chr(val[right])
        return letters[0]
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # ls1=list(set(target))
        # ls2=list(set(arr))
        target.sort()
        arr.sort()
        if target==arr:
            return True
        return False
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        alice=0
        bob=0
        flag=True
        while(len(piles)!=0):
            if piles[0]>piles[-1]:
                if flag:
                    alice+=piles[0]
                else:
                    bob+=piles[0]
                piles.pop(0)
            else:
                if flag:
                    alice+=piles[-1]
                else:
                    bob+=piles[-1]
                piles.pop()
            flag!=flag
        
        if alice>bob:
            return True
        return False
        
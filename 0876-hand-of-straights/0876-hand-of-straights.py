class Solution:
    import heapq
    import copy
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        prev=[]
        if(len(hand)%groupSize!=0):
            return False
        heap=hand
        heapq.heapify(heap)
        ls=[]
        # print(heap)
        while(heap and heap!=prev):
            prev=copy.deepcopy(hand)
            bal=[]
            while(len(ls)<groupSize and heap):
                val=heapq.heappop(heap)
                if len(ls)==0:
                    ls.append(val)
                else:
                    if ls[-1]+1==val:
                        ls.append(val)
                    else:
                        bal.append(val)
            if len(ls)==groupSize:
                ls=[]
            # print(heap,bal)
            while(bal):
                val=bal.pop()
                heapq.heappush(heap,val)
            # print(heap)
            if(prev==heap):
                break
        if len(heap)==0:
            return True
        return False

        
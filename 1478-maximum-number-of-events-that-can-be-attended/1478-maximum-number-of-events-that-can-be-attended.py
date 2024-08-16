class Solution(object):
    import heapq
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        ls=[]
        i=0
        curr_day=0
        event=0
        # print(events)
        while(i<len(events) or ls):   
            # print(i)     
            if not ls:
                curr_day = events[i][0]
            while(i<len(events) and events[i][0]<=curr_day):
                heapq.heappush(ls,events[i][1])
                i+=1
            heapq.heappop(ls)
            event+=1
            curr_day+=1
            # print(ls,event)
            while(ls and ls[0]<curr_day):
                heapq.heappop(ls)
        return event

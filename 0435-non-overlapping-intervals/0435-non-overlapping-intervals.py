class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort_arr=[]
        # while(intervals):
        #     min_ind=0
        #     min_val=float("inf")
        #     # print(intervals)
        #     for i in range(len(intervals)):
        #         if intervals[i][1]<min_val:
        #             min_val=intervals[i][1]
        #             min_ind=i
        #     sort_arr.append(intervals[min_ind])
        #     intervals.pop(min_ind)
        # print(sort_arr)
        sort_arr=intervals
        sort_arr.sort(key=lambda x:x[1])
        cou=0
        if len(sort_arr)>0:
            prev_end=sort_arr[0][1]
            for i in range(1,len(sort_arr)):
                if prev_end>sort_arr[i][0]:
                    cou=cou+1
                else:
                    prev_end=sort_arr[i][1]
        return cou

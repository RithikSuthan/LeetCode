from datetime import datetime, timedelta
from typing import List

class Solution: 
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        minutes = []
        for time in timePoints:
            time_obj = datetime.strptime(time, "%H:%M")
            total_minutes = time_obj.hour * 60 + time_obj.minute
            minutes.append(total_minutes)
        minutes.append(minutes[0] + 1440)
        min_diff = float('inf')
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        return min_diff

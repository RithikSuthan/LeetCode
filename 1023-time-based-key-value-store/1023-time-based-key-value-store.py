class TimeMap:
    stamp={}
    def __init__(self):
        self.stamp={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.stamp:
            self.stamp[key].append([value,timestamp])
        else:
            self.stamp[key]=[[value,timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.stamp:
            l=len(self.stamp[key])
            for i in range(l-1,-1,-1):
                if self.stamp[key][i][1] <=timestamp:
                    return self.stamp[key][i][0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
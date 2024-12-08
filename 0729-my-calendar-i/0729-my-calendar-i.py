class MyCalendar:
    def __init__(self):
        self.ls=[]

    def book(self, start: int, end: int) -> bool:
        # print(self.ls)
        for ele in self.ls:
            if not (end <= ele[0] or start >= ele[1]):
                return False

        self.ls.append((start,end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
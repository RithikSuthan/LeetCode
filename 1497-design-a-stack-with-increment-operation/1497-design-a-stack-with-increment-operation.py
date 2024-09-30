class CustomStack:

    def __init__(self, maxSize: int):
        self.st=[]      
        self.maxSize=maxSize  

    def push(self, x: int) -> None:
        # print("push",self.st)
        if self.st and  len(self.st)>= self.maxSize:
            pass
        else:
            self.st.append(x)

    def pop(self) -> int:
        # print("pop",self.st)
        if self.st:
            return self.st.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        if self.st:
            ind=0
            # print("inc",self.st)
            while ind<len(self.st) and ind<k:
                self.st[ind]=self.st[ind]+val
                ind+=1




# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
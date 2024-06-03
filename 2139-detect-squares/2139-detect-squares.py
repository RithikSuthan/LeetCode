class DetectSquares(object):
    
    def __init__(self):
        self.dict1={}

    def add(self, point):
        x=point[0]
        y=point[1]
        if (x,y) in self.dict1:
            self.dict1[(x,y)]+=1
        else:
            self.dict1[(x,y)]=1

    def count(self, point):
        square=0
        x=point[0]
        y=point[1]
        for i in self.dict1:
            if abs(i[0]-x)==abs(i[1]-y) and i[0]!=x:
                if (i[0],y) in self.dict1 and (x,i[1]) in self.dict1:
                    square=square+self.dict1[(i[0],i[1])]*self.dict1[(i[0],y)]*self.dict1[(x,i[1])]
        return square


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
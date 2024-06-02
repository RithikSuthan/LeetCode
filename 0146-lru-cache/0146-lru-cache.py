class LRUCache:
    from collections import OrderedDict
    def __init__(self, capacity: int):
        self.ls=OrderedDict()
        self.capacity=capacity
    def get(self, key: int) -> int:
        if key in self.ls:
            self.ls.move_to_end(key,last=False)
            return self.ls[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.ls or len(self.ls)<self.capacity:
            self.ls[key]=value
        else:
            self.ls.popitem(last=True)
            self.ls[key]=value
        self.ls.move_to_end(key,last=False)


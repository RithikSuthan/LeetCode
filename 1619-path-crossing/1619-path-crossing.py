class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited=set()
        visited.add((0,0))
        x=0
        y=0
        for dir in path:
            if dir=='N':
                x+=1
            elif dir=='S':
                x-=1
            elif dir=='E':
                y+=1
            elif dir=='W':
                y-=1
            if (x,y) in visited:
                return True
            visited.add((x,y))
            # print(visited)
        return False
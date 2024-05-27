class Solution:
    from collections import deque
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=len(board)
        cols=len(board[0])
        visited=set()
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(i,j):
            queue=deque()
            queue.append((i,j))
            ele=[]
            while(queue):
                curr=queue.popleft()
                visited.add((curr[0],curr[1]))
                ele.append((curr[0],curr[1]))
                for i in directions:
                    u=curr[0]+i[0]
                    v=curr[1]+i[1]
                    if u in range(1,rows-1) and v in range(1,cols-1) and board[u][v]=='O' and (u,v) not in queue and (u,v) not in visited:
                        queue.append((u,v))
            return ele
        for i in range(1,rows-1):
            for j in range(1,cols-1):
                if board[i][j]=='O' and (i,j) not in visited:
                    ele=dfs(i,j)
                    flag=False
                    for k in ele:
                        for z in directions:
                            u=k[0]+z[0]
                            v=k[1]+z[1]
                            if board[u][v]=='O' and ((u==0 or u==rows-1) or (v==0 or v==cols-1)):
                                flag=True
                    if not flag:    
                        for k in ele:
                            board[k[0]][k[1]]='X'
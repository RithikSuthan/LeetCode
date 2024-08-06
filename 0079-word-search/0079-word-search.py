class Solution:
    from collections import deque
    def exist(self, board: List[List[str]], word: str) -> bool:
        queue=deque()
        visited=set()
        rows=len(board)
        cols=len(board[0])
        def dfs(i,j,k):
            if k== len(word):
                return True
            if(i<0 or i>=rows or j<0 or j>=cols or word[k]!=board[i][j] or(i,j) in visited):
                return False
            visited.add((i,j))
            if(dfs(i-1,j,k+1) or dfs(i+1,j,k+1)) or dfs(i,j-1,k+1) or dfs(i,j+1,k+1):
                return True
            visited.remove((i,j))

        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0]:
                    result=dfs(i,j,0)
                    if result:
                        return True
        return False
                
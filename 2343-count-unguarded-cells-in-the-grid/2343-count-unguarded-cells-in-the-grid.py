from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize grid as m x n
        grid = [[0] * n for _ in range(m)]

        # Place guards (1) and walls (2) on the grid
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        # Function to mark cells guarded in all directions
        def mark_guarded(row, col):
            # Mark downward
            for r in range(row + 1, m):
                if grid[r][col] in [1, 2]:  # Stop at guard or wall
                    break
                grid[r][col] = 3
            # Mark upward
            for r in range(row - 1, -1, -1):
                if grid[r][col] in [1, 2]:
                    break
                grid[r][col] = 3
            # Mark rightward
            for c in range(col + 1, n):
                if grid[row][c] in [1, 2]:
                    break
                grid[row][c] = 3
            # Mark leftward
            for c in range(col - 1, -1, -1):
                if grid[row][c] in [1, 2]:
                    break
                grid[row][c] = 3

        # Mark all guarded cells
        for row, col in guards:
            mark_guarded(row, col)

        # Count unguarded cells
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:  # Count only unguarded cells
                    ans += 1
        return ans

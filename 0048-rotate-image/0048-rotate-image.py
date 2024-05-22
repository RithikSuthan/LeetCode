class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        for i in range(m):
            for j in range(i+1):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(m):
            matrix[i]=matrix[i][m::-1]
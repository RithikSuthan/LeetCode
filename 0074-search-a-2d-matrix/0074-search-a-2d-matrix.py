class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l=0
        h=len(matrix[0])
        rows=len(matrix)
        cols=len(matrix[0])
        row=0
        col=cols-1
        while(row in range(0,rows) and col in range(0,cols)):
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                col=col-1
            else:
                row=row+1
        return False
            
        
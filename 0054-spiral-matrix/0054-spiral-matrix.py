class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        controw,contcol=0,0
        result=[]

        while controw < len(matrix) - controw and contcol < len(matrix[0]) - contcol:
            row=controw
            col=contcol
            while(col<len(matrix[0])-contcol):
                result.append(matrix[row][col])
                col+=1
            row+=1
            col-=1
            print("1",result)
            while(row<len(matrix)-controw):
                result.append(matrix[row][col])
                row+=1
            print("2",result)
            col-=1
            row-=1
            print(row,"controw",controw,col,"contcol",contcol)
            if controw < len(matrix) - controw - 1:
                while(col>=contcol):
                    result.append(matrix[row][col])
                    col-=1
            # print("3",result)
                row-=1
                col+=1
            if contcol < len(matrix[0]) - contcol - 1:
                while(row>controw):
                    print(row,col,result)
                    result.append(matrix[row][col])
                    row-=1
            print("4",result)
            controw+=1
            contcol+=1
        return result

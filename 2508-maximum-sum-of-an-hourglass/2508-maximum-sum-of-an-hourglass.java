class Solution {
    public int maxSum(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int max_sum = Integer.MIN_VALUE;
        for(int i = 1 ; i < rows-1 ; i++)
        {
            for (int j = 1 ; j < cols-1 ; j++)
            {
                int curr = grid[i][j]                
                         + grid[i - 1][j - 1]       
                         + grid[i - 1][j]           
                         + grid[i - 1][j + 1]       
                         + grid[i + 1][j - 1]       
                         + grid[i + 1][j]           
                         + grid[i + 1][j + 1]; 
                max_sum = Math.max(max_sum,curr);
                // System.out.println(curr);
            }
        
    }
    // System.out.println(max_sum);
    return max_sum;
    }
}
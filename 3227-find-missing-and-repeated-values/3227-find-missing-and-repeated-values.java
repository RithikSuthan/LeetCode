class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int l = grid.length;
        // System.out.println(l);
        int [] ans = new int[2];
        int [] arr = new int[l * l];
        for(int i = 0;i < l; i++)
        {
            for(int j = 0;j < l; j++)
            {
                int val = grid[i][j];
                if (arr[val - 1] != 0)
                    ans[0] = val;
                arr[val - 1] = val;
            }
        }
        for(int i = 0;i < arr.length; i++)
        {
            if(arr[i] == 0)
                {
                    ans[1] = i + 1;
                    break;
                }
        }
        return ans;
    }
}
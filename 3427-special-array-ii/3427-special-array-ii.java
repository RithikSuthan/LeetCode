class Solution {
    public boolean[] isArraySpecial(int[] nums, int[][] queries) {
        int [] prefix = new int[nums.length];
        for (int i = 1; i < nums.length; i++)
        {
            if (nums[i] % 2 == nums[i-1] % 2)
            {
                prefix[i] = prefix[i-1] + 1;
            }
            else
            {
                prefix[i] = prefix[i-1];
            }
        }

        boolean [] ans = new boolean[queries.length];
        for(int i = 0 ; i < queries.length ; i++)
        {
            int start = queries[i][0];
            int end =  queries[i][1];

            if (prefix[end] != prefix[start])
            {
                ans[i] = false;
            }
            else
            {
                ans[i] = true;
            }

        }
        return ans;
    }
}
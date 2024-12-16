class Solution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        while(k != 0)
        {
            int min_val = Arrays.stream(nums).min().getAsInt();
            for(int i = 0; i < nums.length; i++)
            {
                if(nums[i] == min_val)
                {
                    nums[i] *=multiplier;
                    break;
                }
            }
            k --;
        }
        return nums;
    }
}
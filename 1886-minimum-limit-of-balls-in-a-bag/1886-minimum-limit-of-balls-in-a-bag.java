class Solution {
    public int bagCounter( int val ,int [] nums) 
    {
        int temp = 0;
        for( int i = 0 ; i < nums.length ; i++)
        {
            temp += Math.ceil((double)nums[i] / val) - 1;
        }
        return temp ;
    }
    public int minimumSize(int[] nums, int maxOperations) {
        int minBalls = 1;
        Arrays.sort(nums);
        int maxBalls = nums[nums.length - 1];
        while ( minBalls < maxBalls )
        {
            int mid = (minBalls + maxBalls) / 2;
            if( bagCounter(mid,nums) <= maxOperations)
            {
                maxBalls = mid;
            }
            else
            {
                minBalls = mid + 1;
            }
        }
        return maxBalls;
    }
}
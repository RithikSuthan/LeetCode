class Solution {
    public int backTrack(int index, int currSum, int [] nums,int target)
    {
        if (index == nums.length)
            return target == currSum ? 1 : 0;
        int add = backTrack(index + 1, currSum + nums[index], nums, target);
        int subtract = backTrack(index + 1, currSum - nums[index], nums, target);
        return add + subtract;
    }
    public int findTargetSumWays(int[] nums, int target) {
           return backTrack(0,0,nums,target);
    }
}
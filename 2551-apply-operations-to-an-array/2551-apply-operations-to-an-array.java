class Solution {
    public int[] applyOperations(int[] nums) {
        for(int i = 0; i < nums.length - 1; i++)
        {
            if( nums[i+1] == nums[i] )
            {
                nums[i] *= 2;
                nums[i+1] = 0;
            }
            // for(int ele : nums){
            //     System.out.print(ele+" ");
            // }
            // System.out.println();
        }
        // System.out.println("Push left");
        int left = 0;
        int [] ans = new int [nums.length];
        for(int i = 0; i < nums.length; i++)
        {
            if(nums[i] != 0){
                ans[left] = nums[i];
                left ++;
            }
        }
        return ans;
    }
}
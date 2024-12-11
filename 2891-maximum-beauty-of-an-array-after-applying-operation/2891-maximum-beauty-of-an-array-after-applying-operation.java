import java.util.*;
class Solution {
    public int maximumBeauty(int[] nums, int k) {
        TreeMap<Integer,Integer> mp = new TreeMap<>();
        for(int i = 0 ;i < nums.length;i++)
        {
            int left = nums[i] - k;
            int right = nums[i] + k + 1;

            mp.put(left, mp.getOrDefault(left,0) + 1);
            mp.put(right, mp.getOrDefault(right,0) - 1);

            // System.out.println(mp);
        }
        
        int maxBeauty = 0;
        int currBeauty = 0;
        Iterator<Map.Entry<Integer,Integer>> itr = mp.entrySet().iterator();
        while(itr.hasNext())
        {
            Map.Entry<Integer,Integer> entry = itr.next();
            currBeauty += entry.getValue(); 
            maxBeauty = Math.max(maxBeauty,currBeauty);
        }
        return maxBeauty;
    }
}
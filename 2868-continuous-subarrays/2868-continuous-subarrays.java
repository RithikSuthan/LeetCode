import java.util.*;

class Solution {
    public long continuousSubarrays(int[] nums) {
        int n = nums.length;
        TreeMap<Integer, Integer> map = new TreeMap<>();
        int left = 0;
        long ans = 0;

        for (int right = 0; right < n; right++) {
            map.put(nums[right], map.getOrDefault(nums[right], 0) + 1);

            while (map.lastKey() - map.firstKey() > 2) {
                int count = map.get(nums[left]);
                if (count == 1) {
                    map.remove(nums[left]);
                } else {
                    map.put(nums[left], count - 1);
                }
                left++;
            }

            ans += (right - left + 1);
        }

        return ans;
    }
}

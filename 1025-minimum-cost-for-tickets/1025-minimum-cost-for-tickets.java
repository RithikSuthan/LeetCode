import java.util.*;
class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        int [] dp = new int[days.length];
        dp[0] = dp[0] = Math.min(costs[0], Math.min(costs[1], costs[2]));;
        for(int i = 1; i < days.length; i ++)
        {
            int Day1 = dp[i-1] + costs[0];
            int Day7 = 0;
            int Day30 = 0;
            int index = i;
            while(index > 0 && (days[index - 1] >= (days[i]-6) ))
                index --;
            Day7 = index == 0? costs[1] :dp[index-1] + costs[1];
                        
            index = i;
            while(index > 0 && (days[index - 1] >= (days[i]-29) ))
                index --;
            Day30 = index == 0? costs[2] :dp[index-1] + costs[2];

            dp[i] = Math.min(Day1,Math.min(Day7,Day30));
            // System.out.println(Arrays.toString(dp));
        }
        return dp[days.length-1];

    }
}
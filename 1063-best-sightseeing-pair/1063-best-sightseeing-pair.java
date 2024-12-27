import java.util.*;
class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        if(values.length == 0)
        {
            return 0;
        }
        int maxVal = values[0];
        int maxScore = 0;
        for(int i = 1; i < values.length; i++)
        {
            maxVal = Math.max(maxVal,values[i-1] + i - 1);
            maxScore = Math.max(maxScore,maxVal + values[i] - i);
        }
        return maxScore;
    }
}
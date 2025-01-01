
class Solution {
    public int maxScore(String s) {
        int [] zeros = new int[s.length()];
        int maxVal = 0;
        for(int i = 1; i < s.length() ; i++)
        {
            int ones = 0;
            zeros[i] += zeros[i-1];
            if(s.charAt(i-1) == '0')
            {
                zeros[i] += 1;
            }
            for(int j = i; j < s.length(); j++)
            {
                if(s.charAt(j)== '1')
                {
                    ones += 1;
                }
            }
            maxVal = Math.max(maxVal, zeros[i] + ones);
        }
        return maxVal;
    }
}
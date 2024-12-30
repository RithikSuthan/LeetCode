class Solution {
    public int countGoodStrings(int low, int high, int zero, int one) {
        int [] dp = new int[high+1];
        dp[0] = 1;
        for(int i = 1; i <= high; i ++)
        {
            int zeroVal = i - zero;
            int oneVal = i - one;
            // System.out.println(zeroVal+" "+oneVal);
            dp[i] =  ((zeroVal >= 0 ? dp[zeroVal] : 0) + (oneVal >= 0 ? dp[oneVal] : 0)) % (1000000007);
        }
        // System.out.println(Arrays.toString(dp));
        int ans = 0;
        for(int i = low; i <= high; i ++)
        {
            ans = (ans + dp[i]) % 1000000007;
        }
        return ans;

    }
}
class Solution {
    public int[] finalPrices(int[] prices) {
        int [] ans = new int[prices.length];
        for(int i = 0 ; i < prices.length ; i++)
        {
            int j = i;
            int result = prices[i];
            for(j = i+1 ; j < prices.length  ; j++)
            {
                if(prices[j] <= prices[i])
                {
                    result = prices[i] - prices[j];       
                    break;
                }

            }
            ans[i] = result;
        }
        return ans;
    }
}
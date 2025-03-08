class Solution {
    public int minimumRecolors(String blocks, int k) {
        int ans = blocks.length();
        int start = 0;
        while((start + k) <= blocks.length()){
            String temp = blocks.substring(start,k + start);
            int w_cou = 0;
            for(int i = 0; i < k; i++)
            {
                if(temp.charAt(i) == 'W')
                    w_cou += 1;
            }
            ans = Math.min(ans , w_cou );
            start ++;
        }
        // System.out.println(ans);
        return ans;
    }
}
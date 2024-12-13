class Solution {
    public long findScore(int[] nums) {
        TreeSet<Integer> st = new TreeSet<>(
            (a,b)-> nums[a]!=nums[b] ? Integer.compare(nums[a],nums[b]) : 
            Integer.compare(a,b)
        );
        for(int i = 0; i < nums.length ;i++)
        {
            st.add(i);
        }
        long score = 0;
        while(!st.isEmpty())
        {
            int ind = st.pollFirst();
            score += nums[ind];
            st.remove(ind);

            if(ind > 0 && st.contains(ind - 1))
            {
                st.remove(ind - 1);
            }
            if((ind < nums.length - 1) && st.contains(ind + 1))
            {
                st.remove(ind + 1);
            }
        }
        return score;
    }
}
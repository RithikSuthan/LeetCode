class Solution {
    public int maxCount(int[] banned, int n, int maxSum) {
        Arrays.sort(banned);
        int ind=Arrays.binarySearch(banned,n);
        if(ind<0)
        {
            ind=-(ind+1)-1;
        }
        // System.out.println("Ind "+ind);
        HashSet<Integer> st=new HashSet<>();
        for(int i=0;i<ind+1;i++)
        {
            st.add(banned[i]);
        }
        // System.out.println(st);
        int prefix=0;
        int cou=0;
        for(int i=1;i<n+1;i++)
        {
            if(!st.contains(i))
            {
                if ((prefix+i)<=maxSum)
                {
                    prefix+=i;
                    cou+=1;
                }
                else
                    break;
            }
        }
        return cou;
    }
}
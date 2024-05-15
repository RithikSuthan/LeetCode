class Solution {
    public int getSum(int a, int b) {
        if (b>0)
        {
        for(int i=0;i<b;i++)
        {
            a++;
        }            
        }
        else
        {
            System.out.println(a);    
            for(int i=0;i>b;i--){
              a--;  
              System.out.println(a);
            }
        }
        return a;
    }
}
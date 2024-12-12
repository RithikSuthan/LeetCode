class Solution {
    public boolean isValid(String s) {
        Stack<String> st = new Stack<>();
       
            for(int i = 0; i < s.length(); i++)
        {
            String target = s.substring(i,i+1);
//            System.out.println(i+" "+st+" "+target);
            if(target.equals("(") || target.equals("[") || target.equals("{"))
            {
                st.add(target);
            }
            else if(st.isEmpty())
            {
                return false; 
            }
            else if(target.equals(")") && st.peek().equals("("))
            {
                st.pop();
            }
            else if(target.equals("}") && st.peek().equals("{"))
            {
                st.pop();
            }
            else if(target.equals("]") && st.peek().equals("["))
            {
                st.pop();
            }
            else
            {
                return false; 
            }
        }
        if(st.isEmpty())
        {
            return true; 
        }
        else
        {return false; 
        }
    }
}
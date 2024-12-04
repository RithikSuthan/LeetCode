import java.util.*;
class Solution {
    public boolean isAnagram(String s, String t) {
        char [] s1=s.toCharArray();
        char t1[]=t.toCharArray();
        Arrays.sort(s1);
        Arrays.sort(t1);
        s=new String(s1);
        t=new String(t1);
        if(s.equals(t))
        {
            return true;
        }
        return false;
    }
}
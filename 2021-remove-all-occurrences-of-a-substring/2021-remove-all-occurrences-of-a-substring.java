class Solution {
    public String removeOccurrences(String s, String part) {
        int l = part.length();
        while (s.indexOf(part) != -1)
       {
            int ind = s.indexOf(part);
            s = s.substring(0,ind) + s.substring(ind + l);
            // System.out.println(s);
       }
       return s;
    }
}
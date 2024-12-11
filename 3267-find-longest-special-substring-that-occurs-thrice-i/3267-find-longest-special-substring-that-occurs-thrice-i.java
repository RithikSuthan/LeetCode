class Solution {
    private boolean isSpecial(String s) {
    char firstChar = s.charAt(0);
    for (char c : s.toCharArray()) {
        if (c != firstChar) {
            return false;
        }
    }
    return true;
}

    public int maximumLength(String s) {
       HashMap<String,Integer> hm = new HashMap<>();
        int size = 0;
        while (size < s.length()) {
            for (int j = 0; j < s.length()-size ; j++) {
                String target = s.substring(j, size +j+ 1);
                if(isSpecial(target) && !hm.containsKey(target))
                {
                    int count = 0;
                    int index = s.indexOf(target);

                    while (index != -1) {
                        count++;
                        index = s.indexOf(target, index + 1);
                    }
                    hm.put(target,count);
                }
            }
            size ++;
        }
        // System.out.println(hm);
        int maxLen = 0;
        Iterator<Map.Entry<String,Integer>> itr = hm.entrySet().iterator();
        while(itr.hasNext())
        {
            Map.Entry<String,Integer> entry = itr.next();
            if(entry.getValue()>=3 && maxLen <entry.getKey().length())
            {
                maxLen =entry.getKey().length();
            }
        }
        if(maxLen == 0)
            maxLen = -1;
        // System.out.println(maxLen);
        return maxLen;
    }
}
class Solution {
    public boolean canConstruct(String s, int k) {
        if(s.length() < k){
            return false;
        }
        Map<Character,Integer> hm = new HashMap<>();
        for(Character temp : s.toCharArray())
        {
            hm.put(temp,hm.getOrDefault(temp,0) + 1);
        }
        System.out.println(hm);
        int cou = 0;
        Iterator<Map.Entry<Character,Integer>> itr = hm.entrySet().iterator();
        while(itr.hasNext())
        {
            Map.Entry<Character,Integer> temp = itr.next();
            if(temp.getValue() % 2 != 0)
                cou +=1;
        }
        if(cou > k)
            return false;
    return true;
    }
}
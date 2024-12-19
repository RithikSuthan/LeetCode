import java.util.*;
class Solution {
    public String repeatLimitedString(String s, int repeatLimit) {
        PriorityQueue<Map.Entry<String,Integer>> pq = new PriorityQueue<>((a,b) -> b.getKey().compareTo(a.getKey()));
        HashMap<String,Integer> hm = new HashMap<>();
        for(int i = 0; i < s.length() ; i++)
        {
            String target = s.substring(i,i+1);
            hm.put(target,hm.getOrDefault(target,0)+1);
        }
        StringBuilder ans = new StringBuilder();
        pq.addAll(hm.entrySet());
        while(!pq.isEmpty())
        {
            Map.Entry<String, Integer> entry = pq.poll();
            if(ans.length() > 0 && entry.getKey().equals(ans.substring(ans.length()-1)))
            {
                // System.out.println("Came to if");
                Map.Entry<String, Integer> temp = entry;
                if(!pq.isEmpty())
                {
                    entry = pq.poll();
                    ans.append(entry.getKey()) ;
                    entry.setValue( entry.getValue() - 1 );
                    if (entry.getValue() != 0)
                        pq.add(entry);
                    entry = temp;
                }
                else {
                    return  ans.toString();
                }
            }
            int count = 0;
            while (entry.getValue() > 0)
            {
                // System.out.println(entry);
                count += 1;
                ans.append(entry.getKey());
                entry.setValue(  entry.getValue() - 1 );
                if ( count == repeatLimit  )
                {
                    if(entry.getValue() > 0)
                    {
                        pq.add(entry);
                    }
                    // System.out.println("Break called "+count);
                    break;
                }
        }
        // System.out.println(" End of PQ "+ans + pq);
    }
    return ans.toString();
    }
}
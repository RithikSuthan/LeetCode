import java.util.*;
class Solution {
    public List<String> stringMatching(String[] words) {
        List <String> arr = new ArrayList<>();
        for(int i = 0; i < words.length; i++){
            for(int j = 0;j < words.length; j++)
            {
                if(words[j].contains(words[i]) && i!=j && !arr.contains(words[i]))
                {
                    arr.add(words[i]);
                    // arr.add(words[j]);
                }
            }
        }
        // System.out.println(arr);
        return arr;
    }
}
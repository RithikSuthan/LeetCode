import java.util.*;
class Solution {
    public int maxChunksToSorted(int[] arr) {
        Stack<Integer> st = new Stack<>();
        int i = 0;
        int max_ = 0;
        while(i < arr.length)
        {
            System.out.println(st);
            max_ = Math.max(max_, arr[i]);
            while(!st.isEmpty() && (st.peek() > arr[i] ))
            {
                st.pop();
            }
            st.push(max_);
            i ++;
        }
        return st.size();
    }
}
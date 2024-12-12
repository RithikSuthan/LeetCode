import static java.util.Collection.*;
class Solution {
    public long pickGifts(int[] gifts, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());

        for( int i = 0; i < gifts.length ; i++)
        {
            pq.add(gifts[i]);
        }
        while(k > 0)
        {
            double temp = Math.pow(pq.peek(),0.5);
            pq.remove(pq.peek());
            pq.add((int)temp);
            k--;
        }
        // System.out.println(pq);
        long ans = 0;
        while (!pq.isEmpty())
        {
            ans += pq.peek();
            pq.remove(pq.peek());
        }
        return ans;
    }
}
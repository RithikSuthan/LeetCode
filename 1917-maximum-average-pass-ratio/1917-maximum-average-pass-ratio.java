class Solution {
    public double maxAverageRatio(int[][] classes, int extraStudents) {
        PriorityQueue<ArrayList<Double>> pq = new PriorityQueue<>(
                (a,b) -> Double.compare(
                        (b.get(1) + 1) / (b.get(2) + 1) - (b.get(1) / b.get(2)),
                        (a.get(1) + 1) / (a.get(2) + 1) - (a.get(1) / a.get(2))
                )
        );
        for(int i = 0;i < classes.length;i ++)
        {
            double l = classes[i][0];
            double r = classes[i][1];
            double improvement = (( (l+1)/(r+1) ) - l/r);
            pq.add(new ArrayList<>(Arrays.asList(improvement, l, r)));
        }
        // System.out.println(" Before "+pq);
        while(extraStudents!=0)
        {
            ArrayList<Double> temp = pq.poll();
            // System.out.println(" Taken "+temp);
            double l = temp.get(1)+1;
            double r = temp.get(2)+1;
            double improvement = (( (l+1)/(r+1) ) - l/r);
            pq.add(new ArrayList<>(Arrays.asList(improvement, l, r)));
            extraStudents --;
            // System.out.println(pq);
        }
        double ans = 0;
        while(!pq.isEmpty())
        {
            ArrayList<Double> temp = pq.poll();
            double l = temp.get(1);
            double r = temp.get(2);
            ans += (l/r);
        }
        ans = ans / classes.length;
        // System.out.println(ans);
        return ans;
    }
}
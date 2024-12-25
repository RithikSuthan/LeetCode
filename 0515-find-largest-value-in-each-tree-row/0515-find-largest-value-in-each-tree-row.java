/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
 import java.util.*;
class Solution {
    public List<Integer> largestValues(TreeNode root) {
        List <Integer> ans = new ArrayList<>();
        Queue<TreeNode> queue = new ArrayDeque<>();
        if (root == null)
        {
            return ans;
        }
        queue.add(root);
        
        while( !queue.isEmpty() )
        {
            int queueSize = queue.size();
            int max1 = Integer.MIN_VALUE;
            for(int i = 0; i < queueSize; i ++)
            {
                TreeNode curr = queue.poll();
                max1 = Math.max(max1,curr.val);
                if( curr.left != null )
                {
                    queue.add(curr.left);
                } 
                if( curr.right != null  )
                {
                    queue.add(curr.right);
                }
            }
            ans.add(max1);
        }
        // System.out.println( ans );
        return ans;
    }
}
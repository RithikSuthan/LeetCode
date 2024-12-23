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
class Solution {
    public static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> currentLevel = new ArrayList<>();

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                currentLevel.add(node.val);

                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            result.add(currentLevel);
        }
        return result;
    }

        public int minSwapsToSort(int[] arr) {
        int n = arr.length;
        int[] sorted = Arrays.copyOf(arr, n);
        Arrays.sort(sorted);
        HashMap<Integer, Integer> indexMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            indexMap.put(arr[i], i);
        }

        int swaps = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == sorted[i]) {
                continue;
            }
            swaps++;

            int correctValue = sorted[i];
            int toSwapIndex = indexMap.get(correctValue);
            indexMap.put(arr[i], toSwapIndex);
            indexMap.put(correctValue, i);
            int temp = arr[i];
            arr[i] = arr[toSwapIndex];
            arr[toSwapIndex] = temp;
        }

        return swaps;
    }
    public int minimumOperations(TreeNode root) {
        int ans = 0;
        List<List<Integer>> lt = levelOrder(root);
        Iterator <List<Integer>> it = lt.iterator();
        while(it.hasNext())
        {
            List<Integer> currentLevel = it.next();
            int[] currentArray = currentLevel.stream().mapToInt(Integer::intValue).toArray();
            ans += minSwapsToSort(currentArray);
        }

        // System.out.println(lt);
        return ans;
    }
}
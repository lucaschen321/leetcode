import java.util.*;

public class BinaryTreeLevelOrderTraversal {
     //
     // Definition for a binary tree node.
     public class TreeNode {
         int val;
         TreeNode left;
         TreeNode right;
         TreeNode(int x) { val = x; }
     }

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        Queue<TreeNode> q = new LinkedList<TreeNode>();

        if (root == null) {
            return ans;
        }

        q.add(root);

        while (!q.isEmpty()) {
            int levelSize = q.size();
            List<Integer> temp = new ArrayList<Integer>();

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = q.remove();
                temp.add(node.val);

                if (node.left != null) {
                    q.add(node.left);
                }
                if (node.right != null) {
                    q.add(node.right);
                }
            }
            ans.add(temp);
        }


        return ans;

    }
}

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int val) { this.val = val; }
}

public class LCA {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // Base case: if the root is null or we've found p or q
        if (root == null || root == p || root == q) {
            return root;
        }

        // Recurse on the left and right subtrees
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);

        // If both left and right are non-null, the current root is the LCA
        if (left != null && right != null) {
            return root;
        }

        // If one side is null, return the other side
        return left != null ? left : right;
    }
}

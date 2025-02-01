package tree;

public class TreeNode {
    int val;  // Value stored in the node
    TreeNode left;  // Reference to the left child
    TreeNode right; // Reference to the right child

    // Constructor to create a node
    public TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}
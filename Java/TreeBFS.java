import java.util.*;

// Define the TreeNode class
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    public TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }

    // Method to insert a value into the binary search tree
    public static TreeNode insert(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        } else {
            if (val < root.val) {
                root.left = insert(root.left, val);
            } else {
                root.right = insert(root.right, val);
            }
        }
        return root;
    }
}

// BFS class with a method to perform level-order traversal
class BFS {
    public List<List<Integer>> bfs(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) {
            return res;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (node != null) {
                    level.add(node.val); // Add current node's value to the level list
                    if (node.left != null) {
                        queue.add(node.left);
                    }
                    if (node.right != null) {
                        queue.add(node.right);
                    }
                }
            }

            if (!level.isEmpty()) {
                res.add(level);
            }
        }

        return res;
    }
}

// Main class to test the functionality
public class Main {
    public static void main(String[] args) {
        TreeNode root = new TreeNode(5);
        root = TreeNode.insert(root, 12);
        root = TreeNode.insert(root, 34);
        root = TreeNode.insert(root, 43);
        root = TreeNode.insert(root, 22);
        root = TreeNode.insert(root, 13);

        BFS search = new BFS();
        System.out.println(search.bfs(root));
    }
}

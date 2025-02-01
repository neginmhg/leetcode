package tree;

public class RemoveLeafNodes {
    public TreeNode leafDelete(TreeNode root){
        //if theres no node- do nothing -tree is empty
        //base case
        if(root==null){
            return null;
        }
        //if root leaf
        if(root.left==null && root.right==null){
            root =null; //remove leaf
            return null;
        }
        root.left= leafDelete(root.left);
        root.right=leafDelete(root.right);


        return root;
    }
    public static void main(String[] args) {
        // Create tree nodes
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
       
        // Call the leafDelete function
        RemoveLeafNodes sol = new RemoveLeafNodes();
        sol.printTree(root); // Print the entire tree
        root = sol.leafDelete(root);

        // Print the result (after leaf nodes are removed)
        System.out.println("Tree after removing leaf nodes:");
        sol.printTree(root); // Print the entire tree
    }
    public void printTree(TreeNode root){
        if(root==null){
            return;
        }
        System.out.println(root.val+" ");
        // Recursively print the left and right subtrees
        printTree(root.left);
        printTree(root.right);

    }
   
}

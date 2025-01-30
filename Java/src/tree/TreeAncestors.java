package tree;
import java.util.*;
/* 
public class TreeAncestors {
    class Node{
        int data;
        Node left;
        Node right;
       public Node(int data){
           this.data =data;
           left=right=null;
       }
   }
    public  List<Integer> res ;
    public TreeAncestors(){
        res = new ArrayList<>();
    }
    public boolean findAncestors(Node root, int target){
        if(root==null){
            return false;
        }
        if(root.data ==target){
            return true;
        }
        if(findAncestors(root.left, target) || findAncestors(root.right, target)){
            res.add(root.data);
            return true;
        }
        return false;
    }
    public List<Integer> getRes(){
        return this.res;
    }
    public static void main(String[] args) {
        // Constructing the binary tree
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.left = new Node(6);
        root.right.right = new Node(7);

        // Target node for which we want to find ancestors
        int target = 5;

        // Print the ancestors of the target node
        TreeAncestors ta = new TreeAncestors();
        System.out.println("Ancestors of " + target + ":");
        ta.findAncestors(root, target);  // Output: 2 1
        System.out.println(ta.getRes());
    }
}
*/
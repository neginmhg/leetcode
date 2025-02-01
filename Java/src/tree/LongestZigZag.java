package tree;

public class LongestZigZag {
    private int maxLength =0;

    public int longestZigzag(TreeNode root){
        dfs(root, -1, 0);
        return maxLength;
    }
    public void dfs(TreeNode cur, int nextDirection, int length){
        //base case
        if(cur==null){
            return;
        }
        //process maxLength whenever dfs calls
        maxLength=Math.max(maxLength, length);

        //last time moved right and nextDirection was left
        if(nextDirection==0){      
            //move left now and set nextdirection to right
            dfs(cur.left, 1, length+1);
            //move right again and set nextdirection to left  - RESET LENGTH
            dfs(cur.right, 0,1);

        //last time moved left and nextdirection was right
        }else if(nextDirection==1){
            //move right now and set nextdirection to left
            dfs(cur.right, 0,length+1);
            //move left again and set nextdirection to right - RESET LENGTH
            dfs(cur.left, 1,1);
        }else{
            dfs(cur.left, 1, 1);
            dfs(cur.right, 0,1);
        }
    }
}

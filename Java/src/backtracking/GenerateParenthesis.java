package backtracking;
import java.util.*;

public class GenerateParenthesis {
    public List<String> generateParenthesis(int n) {
        ArrayList<String> res = new ArrayList<>();
        backtrack(0,0,new ArrayList<>(), res,n);
        return res;
    }
    public void backtrack(int open, int closed ,ArrayList<Character> path, ArrayList<String> res, int n){
        if(closed==n && open==n){
            
          // Convert ArrayList<Character> to a String
          StringBuilder sb = new StringBuilder();
          for (char c : path) {
              sb.append(c);
          }
          res.add(sb.toString()); // Add the converted String to the result
          return;
        }
        if(open<n){
            path.add('(');
            backtrack(open+1,closed,path, res,n);
            path.remove(path.size()-1);
        }
        if(closed<open){
            path.add(')');
            backtrack(open,closed+1,path, res,n);
            path.remove(path.size()-1);
        }
    }
}
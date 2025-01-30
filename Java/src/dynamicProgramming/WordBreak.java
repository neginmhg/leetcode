package dynamicProgramming;
import java.util.*;

public class WordBreak {
    public static boolean wordBreakf(String s, List<String> wordDict) {
        //create a dp array with size+1
        boolean[] dp = new boolean[s.length()+1];
        for(int i=0;i<s.length()+1;i++){
            dp[i] =false;
        }
        //base case: empty string
        dp[s.length()]=true;

        //loop S backward char by char
        for(int i=s.length()-1;i>=0;i--){
            //for each char check all words in dict
            for(String word: wordDict){
                if(i+word.length()<=s.length() && s.substring(i,i+word.length()).equals(word)){
                    dp[i] = dp[i+word.length()];
                }
                if(dp[i]){
                    break;
                }
            }
        }
        return dp[0];




    }

    public static void main(String[] args){
        List<String> list = new ArrayList<>();
        list.add("leet");
        list.add("code");
        boolean res = wordBreakf("leetcode", list);
        System.out.println(res);
    }
}

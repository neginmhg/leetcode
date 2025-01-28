import java.util.*;

public class WordBreak {
    public boolean wordBreakf(String s, List<String> wordDict) {
        //create a dp array with size+1
        boolean[] dp = new boolean[s.length()+1];

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
}

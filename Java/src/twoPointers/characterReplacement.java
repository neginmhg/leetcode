package twoPointers;
import java.util.*;
public class characterReplacement {
    public int repl(String s, int k){
        //count map for character to int count
        HashMap<Character, Integer> count =new HashMap<>();
        int res =0;

        //sliding window l,r=0 increase r
        //formula: (r-l+1) - maxFreq<= k
            //if not shrink the window
            //if yes expand the window
        int maxFreq =0;
        int l=0;
        for (int r = 0; r < s.length(); r++) {
            //add count for char at r
            char newChar = s.charAt(r);
            int newCharCount = count.getOrDefault(newChar,0)+1;
            count.put(newChar,newCharCount );

            //update maxFreq to see if new char is max or not
            maxFreq = Math.max(maxFreq, newCharCount);
            //if formula not true shrink
            while((r-l+1) - maxFreq > k){
                //shrink
                char leftC = s.charAt(l);
                count.put(leftC,(count.get(leftC)-1));
                if(count.get(leftC)==0){
                    count.remove(leftC);
                }
                l++;
            }
            res = Math.max(r-l+1, res);

        }
        return res;
    }
}

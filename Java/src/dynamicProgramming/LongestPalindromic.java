package dynamicProgramming;
public class LongestPalindromic {

    public String longestPalindrome(String s) {
        if(s==null || s.length()<1){
            return "";
        }
        int maxLen =0;
        String res="";
        for(int i=0; i<s.length();i++){
            //odd length
            int l=i;
            int r =i;
            while (l>=0 && r<s.length() && s.charAt(l)==s.charAt(r)){
                if(maxLen<=r-l+1){
                    maxLen = r-l+1;
                    res = s.substring(l,r+1);
                }
                maxLen = Math.max(maxLen, r-l+1);
                l--;
                r++;
            }


            //even length
             l=i;
             r =i+1;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > maxLen) {
                    maxLen = r - l + 1;
                    res = s.substring(l, r + 1); // Update result with the new palindrome
                }
                l--;
                r++;
            }
            
        }

        return res;
    }
}
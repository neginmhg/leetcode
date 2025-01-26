import java.util.HashSet;

class longestSubstringNoRepeat {
    public int lengthOfLongestSubstring(String s) {
        int l=0;
        int maxLength =0;
        HashSet<Character> set= new HashSet<>();
        for (int r=0;r<s.length();r++){
            while(set.contains(s.charAt(r))){
                set.remove(s.charAt(l));
                l++;
            }
            set.add(s.charAt(r));
            maxLength = Math.max(maxLength,r-l+1);
        }
        return maxLength;
    }

    public static void main(String args[]){
        longestSubstringNoRepeat solution= new longestSubstringNoRepeat();
        int max =solution.lengthOfLongestSubstring("abcabcbb");
        System.out.println(max);
    }
}
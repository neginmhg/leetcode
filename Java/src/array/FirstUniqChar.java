package array;
import java.util.HashMap;


class FirstUniqChar {
    public int firstUniqChar(String s) {
        //turn string to map of char and count
        //loop through map and return the first char with count=1
        HashMap<Character, Integer> map = new HashMap<>();
        char[] charArray = s.toCharArray();

        for(char c: charArray){
            int count=map.getOrDefault(c, 0);
            map.put(c, count+1);
        }
        int result=-1;
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(map.get(c)==1){
                result= i;
                break;
            }
        }
        return result;
    }
}
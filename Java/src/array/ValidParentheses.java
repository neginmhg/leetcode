package array;
import java.util.*;
class Solution{
    
    public static boolean isValid(String s){
        Map<Character, Character> map = new HashMap<>();
        map.put(')','(');
        map.put(']','[');
        map.put('}','{');
        Stack<Character> stack= new Stack<>();

        char[] chars = s.toCharArray();
        for (char c:chars){
            //if c is opening
            if(map.containsValue(c)){
                stack.push(c);
            }else{
                //c is close
                if(!stack.isEmpty()){
                    char topOpen = stack.pop();
                    if(map.get(c)!=(topOpen)){
                        return false;
                    }
                }else{
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
    public static void main(String []argh)
    {
        Scanner sc = new Scanner(System.in);
        
        while (sc.hasNext()) {
            String input=sc.next();
            System.out.println(isValid(input));
        }
        sc.close();
        
    }
}




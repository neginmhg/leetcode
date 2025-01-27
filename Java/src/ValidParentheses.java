
import java.util.*;

class ValidParentheses {
    public  boolean isValid(String s) {
        Stack<Character> stack= new Stack<>();
        HashMap <Character, Character> map = new HashMap<>();
        map.put(')','(');
        map.put('}', '{');
        map.put(']', '[');

        char[] charArray = s.toCharArray();
        System.out.println(charArray);
        for(char c: charArray){
            if(map.containsValue(c)){
                stack.push(c);
            }else if(map.containsKey(c)){
                char topE = stack.isEmpty()? '#' : stack.pop();
                if(topE != map.get(c)){
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }

    public static void main(String[] args){
        ValidParentheses solution = new ValidParentheses();
        System.out.println(solution.isValid("()"));       // Output: true
        System.out.println(solution.isValid("()[]{}"));   // Output: true
        System.out.println(solution.isValid("(]"));       // Output: false
    }
}
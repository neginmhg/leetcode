import java.util.*;
public class CustomStack {
    //fields
    private List<Integer> stack;
    private List<Integer> minStack;
    private List<Integer> maxStack;

    //constructor
    public CustomStack(){
        this.stack = new ArrayList<>();
        this.minStack = new ArrayList<>();
        this.maxStack = new ArrayList<>();
    }


    //push method
    public void push(int x){
        stack.add(x);   //add will add x to end of array list-rightmost

        int lastIndexMin = minStack.size()-1;
        if(minStack.isEmpty() || x<minStack.get(lastIndexMin)){
            minStack.add(x);
        }else{
            minStack.add(stack.get(lastIndexMin));
        }
       // Update the maxStack
       int lastIndexMax = maxStack.size()-1;
       if (maxStack.isEmpty() || x >= maxStack.get(lastIndexMax)) {
        maxStack.add(x);
        } else {
            maxStack.add(maxStack.get(lastIndexMax));
        }

    }

    //pop method
    public int pop(){
        if(stack.isEmpty()){
            return -1;
        }
        int lastIndexMin = minStack.size()-1;
        int lastIndexMax = maxStack.size()-1;
        minStack.remove(lastIndexMin);
        maxStack.remove(lastIndexMax);
        int res=stack.removeLast();
        return res;
    }

    public int peek(){
        if (stack.isEmpty()) {
            return -1;
        }
        return stack.getLast();
    }

    // Get the minimum element in the stack
    public int getMin() {
        if (minStack.isEmpty()) {
            System.out.println("Stack is empty");
            return Integer.MAX_VALUE;  // Return max value if stack is empty
        }
        return minStack.get(minStack.size() - 1);
    }

    // Get the maximum element in the stack
    public int getMax() {
        if (maxStack.isEmpty()) {
            System.out.println("Stack is empty");
            return Integer.MIN_VALUE;  // Return min value if stack is empty
        }
        return maxStack.get(maxStack.size() - 1);
    }
}

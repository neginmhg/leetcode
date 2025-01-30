
import java.util.*;
public class basics{
    public static void main(String args[]){
        // Array
        int[] nums = {1,2,3,4,5};
        int[] nums2 = new int[5];   //array of size 5
        int[][] matrix = new int[3][3]; //matrix of 3*3
        int[][] matrix2 = {{1,2},{3,4},{5,6}};

        for (int i = 0; i < nums.length; i++) {
            System.out.println(nums[i]);
        }
        for (int num : nums) {
            System.out.println(num);
        }
        int[] newNums= Arrays.copyOf(nums, nums.length);

        //Filling array 
        Arrays.fill(nums,0);
        
        System.out.println("Array: " + Arrays.toString(nums));
        nums[0]=10;
        System.out.println("Updated Array: " + Arrays.toString(nums));
        Arrays.sort(nums);
        System.out.println("Sorted Array: " + Arrays.toString(nums));
        System.out.println("Binary Search (3): " + Arrays.binarySearch(nums, 3));


        // ArrayList - dynamic array
        ArrayList<Integer> al=new ArrayList<>();
        //add , remove(indx), get(indx), set(indx,val), contains(val), indexOf(val)
        //isEmpty, size
        al.add(10);
        al.add(20);
        //[10, 20]
        al.add(1,15);   //add 15 at index 1
        //[10, 15, 20]
        al.remove(0);    //remove by index
        //[15, 20]
        al.get(1); //res=20
        al.set(1,200);  //update val at index 0
        System.out.println("Size: " + al.size()); //size=2
        System.out.println("Contains 20: " + al.contains(20)); //true
        al.clear();
        System.out.println("ArrayList after clear: " + al);


        // 3. LinkedList (Doubly linked list)
        LinkedList<Integer> ll = new LinkedList<>();
        //add, get , remove, isEmpty, size  
        ll.add(100);        //add to the end
        ll.add(3,500);         // to index 3 value 500
        ll.addFirst(50); //add to the beginning
        ll.addLast(150); //add to the end
        ll.offer(400);  //add to the end and return true/false
        ll.offerFirst(500);
        ll.offerLast(600);
        int res=ll.getFirst();
        res = ll.get(2);  //retrive elment at index 2
        res = ll.getLast();
        res = ll.peek();    //view the first element
        ll.remove();        //remove first element/head
        ll.remove(3);   //remove at index 3
        ll.poll();  //remove the head of the list
        ll.removeFirst(); // Remove first element
        ll.removeLast(); // Remove last element
        System.out.println("LinkedList after removals: " + ll);
        ll.clear();     //empty the list



         // 4. HashMap (Key-Value pair)
         HashMap<String, Integer> hashMap=new HashMap<>();
         //put, remove, get(key), containsKey(key) , containsValue(val)
         hashMap.put("Alice", 30); // Add key-value pair
         hashMap.put("Bob", 25);
         hashMap.put("Charlie", 35);
         System.out.println("HashMap: " + hashMap);
         System.out.println("Get value for 'Bob': " + hashMap.get("Bob"));
        System.out.println("Contains key 'Alice': " + hashMap.containsKey("Alice"));
        System.out.println("Contains value 35: " + hashMap.containsValue(35));
        hashMap.remove("Alice"); // Remove key
        System.out.println("HashMap after removal: " + hashMap);



        // 5. HashSet (Unique elements)
        HashSet<Integer> hashSet = new HashSet<>();
        //add, remove, contains(v)
        hashSet.add(1); // Add element
        hashSet.add(2);
        hashSet.add(2); // Duplicate (ignored)
        System.out.println("HashSet: " + hashSet);
        // Methods:
        System.out.println("Contains 2: " + hashSet.contains(2));
        hashSet.remove(1); // Remove element
        System.out.println("HashSet after removal: " + hashSet);
        hashSet.clear(); // Clear all elements
        System.out.println("HashSet after clear: " + hashSet);


        // 6. Stack (Last-In-First-Out)
        Stack<Integer> stack = new Stack<>();
        //push,pop, peek, isEmpty, size
        stack.push(5); // Push element
        stack.push(10);
        System.out.println("Stack (peek): " + stack.peek()); // Peek at the top
        stack.pop(); // Remove the top element
        System.out.println("Stack after pop: " + stack);

        // Methods:
        System.out.println("Is Stack Empty: " + stack.isEmpty());


         // 7. Queue (First-In-First-Out)
         Queue<Integer> queue = new LinkedList<>();
         //add, poll, peek, isEmpty, size
         queue.add(15); // Add element
         queue.add(30);
         System.out.println("Queue (peek): " + queue.peek()); // Peek at the front
         queue.poll(); // Remove the front element
         System.out.println("Queue after poll: " + queue);
         // Methods:
         System.out.println("Is Queue Empty: " + queue.isEmpty());
         System.out.println("Queue Size: " + queue.size());

        // 8. PriorityQueue (Min-Heap by default)
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        //add, poll, peek, isEmpty ,size
        priorityQueue.add(10); // Add element
        priorityQueue.add(5);
        priorityQueue.add(20);
        System.out.println("PriorityQueue (peek): " + priorityQueue.peek()); // Peek smallest element
        priorityQueue.poll(); // Remove smallest element
        System.out.println("PriorityQueue after poll: " + priorityQueue);
        System.out.println("Is PriorityQueue Empty: " + priorityQueue.isEmpty());
        System.out.println("PriorityQueue Size: " + priorityQueue.size());


        // 9. Deque (Double-Ended Queue)
        Deque<Integer> deque = new ArrayDeque<>();
        deque.addFirst(10); // Add at the beginning
        deque.addLast(20); // Add at the end
        System.out.println("Deque: " + deque);
        deque.removeFirst(); // Remove from the beginning
        deque.removeLast(); // Remove from the end
        System.out.println("Deque after removals: " + deque);
        deque.add(30); // Add element (acts as a queue)
        System.out.println("Deque (peek): " + deque.peek());
        deque.poll(); // Remove first element
        System.out.println("Deque after poll: " + deque);

        // 10. TreeMap (Sorted Key-Value pair)
        TreeMap<String, Integer> treeMap = new TreeMap<>();
        treeMap.put("Banana", 1); // Add key-value pair
        treeMap.put("Apple", 2);
        treeMap.put("Cherry", 3);
        System.out.println("TreeMap: " + treeMap);
        System.out.println("First Key: " + treeMap.firstKey());
        System.out.println("Last Key: " + treeMap.lastKey());
        treeMap.remove("Banana"); // Remove key
        System.out.println("TreeMap after removal: " + treeMap);


        // 1. String Initialization using Literal
        String str1 = "Hello";  // String literal (interned in the String pool)
        System.out.println("Literal String: " + str1);
        
        // 2. String Initialization using new keyword
        String str2 = new String("Hello");  // Creates a new String object (not interned)
        System.out.println("New String: " + str2);

        // 3. String Immutability: Strings are immutable
        String str3 = "World";
        str3 = str3.concat("!");  // A new string "World!" is created, str3 is now pointing to it
        System.out.println("Concatenated String: " + str3);

        // 4. String Methods
        System.out.println("Length of str1: " + str1.length());  // Returns the length of the string
        System.out.println("Char at index 1 in str1: " + str1.charAt(1));  // Returns the character at index 1
        
        // Substring: Extracts a part of the string from index 0 to 3 (exclusive)
        String substring = str1.substring(0, 3);  
        System.out.println("Substring of str1: " + substring);  // Output: Hel
        
        // Replace characters in string
        String replaced = str1.replace("e", "a");
        System.out.println("Replaced String: " + replaced);  // Output: Hallo
        
        // Trim: Removes leading and trailing spaces
        String str4 = "   Hello   ";
        System.out.println("Trimmed String: " + str4.trim());  // Output: "Hello"
        
        // Convert to Uppercase and Lowercase
        System.out.println("Uppercase: " + str1.toUpperCase());  // Output: HELLO
        System.out.println("Lowercase: " + str1.toLowerCase());  // Output: hello
        
        
        char[] chars = {'H', 'e', 'l', 'l', 'o'};
        String str9 = new String(chars);  // "Hello"

        // String Comparison (equals and ==)
        //String str5 = "Hello";
        String str6 = new String("Hello");
        System.out.println("str1 == str2? " + (str1 == str6));  // false, because they are different objects
        System.out.println("str1.equals(str2)? " + str1.equals(str6));  // true, because they have the same content
        
        // StringBuilder usage (mutable string)
        StringBuilder sb = new StringBuilder("Hello");
        sb.append(" World");  // Mutates the existing StringBuilder object
        System.out.println("StringBuilder: " + sb.toString());  // Output: Hello World
        
        // String Conversion: String to number
        int num = Integer.parseInt("42");
        System.out.println("Converted String to Integer: " + num);  // Output: 42
        
        // Convert number to String
        String numStr = String.valueOf(42);
        System.out.println("Converted Integer to String: " + numStr);  // Output: "42"
        
        // String Pool: Demonstrating String interning
        String str7 = "Hello";
        //String str8 = "Hello";
        System.out.println("str1 == str2 (same reference in pool)? " + (str1 == str7));  // true, both refer to the same string in the pool
        
        // Formatting Strings
        String formatted = String.format("Hello %s, your age is %d", "John", 25);
        System.out.println("Formatted String: " + formatted);  // Output: "Hello John, your age is 25"
        
        // printf: Direct formatting to console
        System.out.printf("Hello %s, your age is %d\n", "John", 25);  // Output: Hello John, your age is 25


        //count freq of a char
        String str = "hello world";
        char target = 'o';
        int count = 0;
        for (char c : str.toCharArray()) {
            if (c == target) count++;
        }
        System.out.println(count);  // Output: 2

        String str99 = "one,two,three";
        String[] parts = str.split(",");
        System.out.println(Arrays.toString(parts));   // Output: [one, two, three]

        String joined = String.join("-", "one", "two", "three");
        System.out.println(joined);                   // Output: "one-two-three"

        String str33 = "  Hello World  ";
        System.out.println(str.trim());                // Output: "Hello World"
        System.out.println(str.toUpperCase());         // Output: "  HELLO WORLD  "
        System.out.println(str.replace('o', 'a'));     // Output: "  Hella Warld  "


        //StringBuilder: Mutable Strings: Modifications like appending, deleting, or replacing are done on the same object, unlike String, which creates a new object for each change.
        StringBuilder sb1 = new StringBuilder(); // Empty StringBuilder
        StringBuilder sb2 = new StringBuilder("Hello"); // Initialized with "Hello"
        StringBuilder sb3 = new StringBuilder(50); // Initial capacity of 50 characters

        //add a string to the end
        StringBuilder sb5 = new StringBuilder("Hello");
        sb5.append(" World");
        System.out.println(sb5);  // Output: Hello World
        sb5.delete(5, 11);
        sb5.reverse();
        StringBuilder sb6 = new StringBuilder("Hello");
        System.out.println(sb6.length());    // Output: 5
        System.out.println(sb6.capacity());  // Output: 21 (default is 16 + initial string length)
        sb6.ensureCapacity(50);              // Ensures capacity is at least 50


        StringBuilder sb4 = new StringBuilder("Hello");
        String str77 = sb4.toString();
        System.out.println(str77);  // Output: Hello




    }



     
}
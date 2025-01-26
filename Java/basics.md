A **table summarizing the operations for each data structure**:

| **Data Structure** | **Operations**                                                                                 |
|---------------------|-----------------------------------------------------------------------------------------------|
| **Array**           | Access: `nums[index]` <br> Modify: `nums[index] = value` <br> Sort: `Arrays.sort(nums)` <br> Search: `Arrays.binarySearch(nums, value)` |
| **ArrayList**       | Add: `add(value)`, `add(index, value)` <br> Access: `get(index)` <br> Remove: `remove(index)` <br> Check: `contains(value)`, `isEmpty()` <br> Size: `size()` |
| **LinkedList**      | Add: `add(value)`, `addFirst(value)`, `addLast(value)` <br> Access: `getFirst()`, `getLast()` <br> Remove: `removeFirst()`, `removeLast()` |
| **HashMap**         | Add: `put(key, value)` <br> Access: `get(key)` <br> Remove: `remove(key)` <br> Check: `containsKey(key)`, `containsValue(value)` |
| **HashSet**         | Add: `add(value)` <br> Remove: `remove(value)` <br> Check: `contains(value)` <br> Clear: `clear()` |
| **Stack**           | Push: `push(value)` <br> Pop: `pop()` <br> Peek: `peek()` <br> Check: `isEmpty()` |
| **Queue**           | Add: `add(value)` <br> Peek: `peek()` <br> Poll: `poll()` <br> Check: `isEmpty()`, `size()` |
| **PriorityQueue**   | Add: `add(value)` <br> Peek: `peek()` <br> Poll: `poll()` <br> Check: `isEmpty()`, `size()` |
| **Deque**           | Add: `addFirst(value)`, `addLast(value)` <br> Remove: `removeFirst()`, `removeLast()` <br> Peek: `peek()` |
| **TreeMap**         | Add: `put(key, value)` <br> Remove: `remove(key)` <br> Access: `firstKey()`, `lastKey()` |




Memorizing all the data structure operations can feel overwhelming, but breaking it into manageable chunks with associations and patterns makes it easier. Here's a structured guide to help you:

---

### **1. Recognize Patterns Across Data Structures**
- **Common Operations**: Notice similarities like `add`, `remove`, `peek`, and `contains` across different structures. These are intuitive and reoccur often.
- Example: `add` and `remove` are present in **ArrayList**, **LinkedList**, **HashSet**, **Deque**, and **Queue**.

---

### **2. Group by Usage**
Group data structures based on their functionality and use case:
- **Sequential Access**: Arrays, ArrayLists, LinkedLists (Use indexing or positional access methods like `get` and `set`).
- **Key-Value Pair**: HashMap, TreeMap (Focus on `put`, `get`, `remove`).
- **Unique Elements**: HashSet (Simple `add`, `remove`, `contains`).
- **Stacks and Queues**: Stack (LIFO: `push`, `pop`, `peek`) and Queue (FIFO: `add`, `poll`, `peek`).

---

### **3. Use Mnemonics**
- **Stacks**: Think **PLP** ("Push, Look, Pop") for `push`, `peek`, `pop`.
- **Queues**: Think **A Peek Poll** ("Add, Peek, Poll").
- **HashMaps**: Associate with a dictionary: You **Put**, then **Get**, or **Remove** entries.
- **TreeMap**: Visualize a sorted dictionary (keys in order): Access the **First** and **Last**.

---

### **4. Leverage Real-Life Analogies**
- **Stack**: A stack of plates (Add to the top, remove from the top).
- **Queue**: A line at a grocery store (First person in line is the first to leave).
- **HashMap**: A phone book (Search by key = name, and find value = phone number).
- **PriorityQueue**: A VIP line (Higher priority leaves first).

---

### **5. Use Flashcards**
Create flashcards with the following format:
- **Front**: "HashMap operations?"
- **Back**: `put(key, value)`, `get(key)`, `remove(key)`, `containsKey(key)`, `containsValue(value)`
Review these daily to solidify your memory.

---

### **6. Implement Them**
- Write **short code snippets** to test each method in your IDE. 
- Example: Write a class with methods to demonstrate all operations for a single data structure.
- Focus on the ones you use less frequently first (e.g., TreeMap or PriorityQueue).

---

### **7. Use Visual Aids**
- Draw diagrams:
  - **Stack**: Draw a vertical stack.
  - **Queue**: Draw elements moving left to right.
  - **HashMap**: Draw a key-value pair table.
- Annotate with operations like `add`, `remove`, etc.

---

### **8. Test Yourself with LeetCode**
- Solve problems for each data structure (filter by tag on LeetCode).
  - **Stacks**: Use for problems like **valid parentheses** or **evaluate postfix expressions**.
  - **Queues**: Try BFS traversal problems.
  - **HashMaps**: Solve problems like finding duplicate elements or frequency counts.

---

### **9. Combine & Simplify**
Here’s a short and combined version:
- **Sequential Access**: Arrays (`get`, `set`), ArrayList (`add`, `remove`, `get`), LinkedList (add/remove at start/end).
- **Key-Value**: HashMap/TreeMap (`put`, `get`, `remove`).
- **Unique Elements**: HashSet (`add`, `remove`, `contains`).
- **Stacks**: Push, pop, peek.
- **Queues**: Add, poll, peek.
- **PriorityQueue**: Like Queue but ordered.
- **Deque**: Add/remove at both ends.

---

### **10. Practice Daily (Short but Consistent)**
Spend 10–15 minutes daily:
1. Write out operations from memory.
2. Test yourself using flashcards.
3. Solve a LeetCode problem focusing on one data structure per day.


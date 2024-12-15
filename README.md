# leetcode


# Mutability in Python

In Python, mutability refers to whether an object's state or value can be changed after it is created. Understanding mutability is important for managing data effectively and avoiding unintended side effects in your programs.

## Mutable Objects (Lists , Dicts, Sets, Custom Obj)

Mutable objects in Python can be modified after they are created. Changes made to a mutable object through one reference affect all other references to that object. Common mutable objects include:

- **Lists (`list`)**: Modified using methods like `append()`, `extend()`, `pop()`, etc.
- **Dictionaries (`dict`)**: Modified using methods like `update()`, `pop()`, or direct assignment.
- **Sets (`set`)**: Modified using methods like `add()`, `remove()`, `discard()`, etc.
- **Custom Objects**: Instances of classes that allow modification of their attributes.

## Immutable Objects (int, str, tuple)

Immutable objects in Python cannot be changed once they are created. Any operation that appears to modify an immutable object actually creates a new object with the modified value. Common immutable objects include:

- **Integers (`int`)** and **Floats (`float`)**: Once created, their values cannot be changed.
- **Strings (`str`)**: Operations like concatenation or slicing create new strings.
- **Tuples (`tuple`)**: Collections whose elements cannot be changed after creation.

## Importance of Mutability

Understanding mutability helps in writing efficient and bug-free code:

- **Side Effects**: Mutable objects can lead to unexpected behavior if shared among different parts of the program.
- **Thread Safety**: Immutable objects are inherently thread-safe.
- **Functional Programming**: Immutability supports functional programming paradigms by facilitating data flow without unintended modifications.

In summary, knowing which objects are mutable and which are immutable allows you to make informed decisions about data management in Python.

# Functions to remember:

- Counter: Count each task and store the counts in a hashmap
  - from typing import Counter, List
  - tasks = List[str]
  - count = Counter(tasks)
- Create a max heap by negating the counts (since heapq is a min heap by default)
  - maxHeap = [-cnt for cnt in count.values()]
- Whenever you want to handle/avoid duplicates

  - consider using set()
  - sort() the array and then handle dup easier

- Intersection operator
  - set1 = {1, 2, 3, 4}
  - set2 = {3, 4, 5, 6}
  - Find the intersection and convert to a list using & operator
  - intersection_list = list(set1 & set2)
  - or use --> intersection_list = list(set1.intersection(set2))
  - print(intersection_list) # Output: [3, 4]
- Union operator
  - set1 = {1, 2, 3, 4}
  - set2 = {3, 4, 5, 6}
  - Find the union and convert to a list using | operator
  - union_list = list(set1 | set2)
  - or use --> union_list = list(set1.union(set2))
  - print(union_list) # Output: [1, 2, 3, 4, 5, 6]
- pair=[[p,s] for p,s in zip(position,speed)]

# Accessing Sets can't be done with Indexes

you **cannot** access elements of a set via indexing in Python.

A **set** in Python is an **unordered collection**, which means the elements do not have a specific order, and as such, you cannot access them by index (like you can with lists or tuples). If you try to access an element of a set using indexing (e.g., `my_set[0]`), you will get a `TypeError`.

### How to Access Elements in a Set:

If you want to access elements from a set, you can:

1. **Iterate over the set**:
   You can use a `for` loop to iterate through the elements.

   ```python
   for elem in my_set:
       print(elem)
   ```

2. **Use `next(iter(set))`**:
   This gives you the "first" element in the set (though it could be any element, since sets are unordered).

   ```python
   my_set = {1, 2, 3}
   first_element = next(iter(my_set))
   print(first_element)
   ```

3. **Convert the set to a list** if you need to access elements via indexing:
   ```python
   my_set = {1, 2, 3}
   my_list = list(my_set)
   print(my_list[0])  # Accessing the first element
   ```

But in general, avoid assuming any specific order when working with sets.

# Accessing Tuples

In Python, you can access elements in a tuple using **indexing** because tuples are ordered collections.

### Syntax for Tuple Indexing:

You use square brackets (`[]`) to access elements at a specific index in the tuple. Indexing starts at `0`, where the first element is at index `0`, the second element at index `1`, and so on. Negative indexing is also supported, where `-1` refers to the last element, `-2` to the second-to-last, etc.

### Example:

```python
my_tuple = (10, 20, 30, 40, 50)

# Access elements using positive indices
print(my_tuple[0])  # Output: 10
print(my_tuple[2])  # Output: 30

# Access elements using negative indices
print(my_tuple[-1])  # Output: 50  (last element)
print(my_tuple[-3])  # Output: 30  (third-to-last element)
```

### Key Points:

- Tuples are **indexed** like lists, with the first element at index `0`.
- You can use both **positive** and **negative** indices to access elements in a tuple.
- Tuples are **immutable**, meaning you can’t change or modify elements once they are created, but you can access them via indexing.

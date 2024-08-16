# leetcode

https://blog.pragmaticengineer.com/my-reading-list/#engineering-career-books

# Mutability in Python

In Python, mutability refers to whether an object's state or value can be changed after it is created. Understanding mutability is important for managing data effectively and avoiding unintended side effects in your programs.

## Mutable Objects

Mutable objects in Python can be modified after they are created. Changes made to a mutable object through one reference affect all other references to that object. Common mutable objects include:

- **Lists (`list`)**: Modified using methods like `append()`, `extend()`, `pop()`, etc.
- **Dictionaries (`dict`)**: Modified using methods like `update()`, `pop()`, or direct assignment.
- **Sets (`set`)**: Modified using methods like `add()`, `remove()`, `discard()`, etc.
- **Custom Objects**: Instances of classes that allow modification of their attributes.

## Immutable Objects

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

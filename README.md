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

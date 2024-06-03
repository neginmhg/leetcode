# Object Copying

In object-oriented programming, object copying is the act of creating and initializing a new object based on an existing object's state. The various ways to implement copy have implications that a programmer needs to understand in order to write a computer program that is correct and performant. Copying allows for the emergent state of the original object – represented by its internal state – to be used and even modified without affecting the original object.

## Strategies

Generally, an object resembles a monolithic concept while having an internal structure that is composite data – a tree of state. Several strategies have been developed to copy this internal state based on program needs and runtime cost. The earliest discussed are shallow and deep copy – with the terminology dating back to Smalltalk-80.

A similar distinction holds for comparing objects for equality. For two objects to be equal, their state must be the same in a meaningful way. Two objects could be considered equal if their fields are equal without traversing into sub-objects (shallow). Or maybe they are considered equal only if the state is equal throughout the object tree (deep).

If two variables contain the same reference value, then clearly they refer to the same object which is even more specific than equal.

### Reference Copy

Even shallower than shallow copy, copying a reference is a form of object copying. This strategy is commonly employed when passing an object to a method. The reference is passed by value – a copy of the reference value (probably an address).

```python
a = [1, 2, 3]
b = a  # Reference copy
b.append(4)
print(a)  # Output: [1, 2, 3, 4]
print(b)  # Output: [1, 2, 3, 4]

```

### Shallow Copy

Shallow copy involves creating a new, uninitialized object, B, and copying each field value from the original, A. Due to this procedure, this is also known as a field-by-field copy, field-for-field copy, or field copy. If the field value is a primitive type (such as int), the value is copied such that changes to the value in B do not affect the value in A. If the field value is a reference to an object (e.g., a memory address) the reference is copied, hence referring to the same object that A does. Changing the state of the inner object affects the emergent state of both A and B since the objects are shared. In a language without primitive types (where everything is an object), all fields of the copy reference the same objects as the fields of the original.

A shallow copy is often relatively simple to implement and computationally cheap to perform. It can usually be implemented by simply copying a contiguous block of memory.

```python
import copy

a = [1, 2, [3, 4]]
b = copy.copy(a)  # Shallow copy
b[2][0] = 'a'
print(a)  # Output: [1, 2, ['a', 4]]
print(b)  # Output: [1, 2, ['a', 4]]

```

### Deep Copy

Deep copy involves copying the state of all subordinate objects – recursively dereferencing object references at each level of the tree that is the state of the original object and creating new objects and copying fields. A modification of either the original or copied object, including their inner objects, does not affect the other since they share no content.

```python
import copy

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)  # Deep copy
b[2][0] = 'a'
print(a)  # Output: [1, 2, [3, 4]]
print(b)  # Output: [1, 2, ['a', 4]]

```

### Hybrid

In more complex cases, some fields in a copy should have shared values with the original object (as in a shallow copy), corresponding to an association relationship; and some fields should have copies (as in a deep copy), corresponding to an aggregation relationship. In these cases a custom implementation of copying is generally required; this issue and solution dates to Smalltalk-80. Alternatively, fields can be marked as requiring a shallow copy or deep copy, and copy operations automatically generated (likewise for comparison operations). This is not implemented in most object-oriented languages, however, though there is partial support in Eiffel.

```python
class MyObject:
    def __init__(self, data, ref):
        self.data = data
        self.ref = ref

    def copy(self):
        # Perform hybrid copy: deep copy for `data` and shallow copy for `ref`
        new_obj = MyObject(copy.deepcopy(self.data), self.ref)
        return new_obj

original = MyObject([1, 2, [3, 4]], {"key": "value"})
copy_obj = original.copy()

```

### Lazy Copy

Lazy copy, related to copy-on-write, is an implementation of a deep copy. When initially copying an object, a relatively fast shallow copy is performed. A counter is also used to track how many objects share the data. When the program wants to modify an object, it can determine if the data is shared (by examining the counter) and can perform a deep copy if needed.

Lazy copy provides the semantics of a deep copy but takes advantage of the speed of a shallow copy when possible. The downside are rather high but constant base costs because of the counter. Circular references can cause problems.

```python
import copy

class CustomObject:
    def __init__(self, value):
        self.value = value

    def __copy__(self):
        # Custom shallow copy implementation
        return CustomObject(self.value)

    def __deepcopy__(self, memo):
        # Custom deep copy implementation
        return CustomObject(copy.deepcopy(self.value, memo))

original = CustomObject([1, 2, 3])
shallow_copied = copy.copy(original)
deep_copied = copy.deepcopy(original)

```

### Examples

Generally, an object-oriented programming language provides a way to copy an object. A programmer must define how a custom-defined object is copied, just as they must define if two objects are equal, comparable and so on. Some languages support one of both of the shallow or deep strategies, defining either one copy operation or separate shallow and deep operations. Many languages provide some default behavior.
<br/><br/><br/><br/>

# The funtions

## 1. **Shallow Copy**: `copy.copy()`

```python
import copy
shallow_copy = copy.copy(original_object)
```

## 2. **Deep Copy**: `copy.deepcopy()`

```python
import copy
deep_copy = copy.deepcopy(original_object)
```

## 3. **Reference Copy**: No specific function, just assigning variables to the same object reference.

```python
reference_copy = original_object
```

## 4. **Hybrid Copy**: Custom implementation within the class.

```python
class CustomObject:
    def hybrid_copy(self):
        # Custom implementation for hybrid copy
        # Return a new object with a mix of shallow and deep copy
```

## 5. **Lazy Copy**: Custom implementation within the class.

```python
class CustomObject:
    def lazy_copy(self):
        # Custom implementation for lazy copy
        # Return a new object with lazy copying behavior
```

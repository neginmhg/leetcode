Explanation of each example with a description of the **lambda function** 

---

### **1. Using `lambda` with `sorted`**
```python
data = [(1, 2), (3, 1), (5, 4)]
data.sort(key=lambda x: x[1])
print(data)  # Output: [(3, 1), (1, 2), (5, 4)]
```
**What the `lambda` does**:  
The `lambda` takes a tuple `x` as input and returns the second element of the tuple (`x[1]`). This is used by the `sorted` function to sort the list based on the second element of each tuple.

---

### **2. Using `lambda` with `map`**
```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # Output: [2, 4, 6, 8]
```
**What the `lambda` does**:  
The `lambda` takes a number `x` as input and returns `x * 2`. This operation is applied to each number in the `nums` list, resulting in a list where each number is doubled.

---

### **3. Using `lambda` with `filter`**
```python
nums = [1, 2, 3, 4, 5]
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums)  # Output: [1, 3, 5]
```
**What the `lambda` does**:  
The `lambda` takes a number `x` as input and returns `True` if `x` is odd (`x % 2 != 0`) and `False` otherwise. The `filter` function keeps only the numbers for which the `lambda` returns `True`.

---

### **4. Using `lambda` with `reduce`**
```python
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 24
```
**What the `lambda` does**:  
The `lambda` takes two numbers, `x` and `y`, and returns their product (`x * y`). The `reduce` function applies this `lambda` cumulatively to the list, calculating the product of all numbers in `nums`.

---

### **5. Sorting Strings by Length**
```python
strings = ["apple", "banana", "cherry"]
strings.sort(key=lambda x: len(x))
print(strings)  # Output: ['apple', 'cherry', 'banana']
```
**What the `lambda` does**:  
The `lambda` takes a string `x` as input and returns its length (`len(x)`). The `sort` function uses this to order the strings by their length.

---

### **6. Dynamic Operations with `map`**
```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Output: [1, 4, 9, 16]
```
**What the `lambda` does**:  
The `lambda` takes a number `x` as input and returns its square (`x**2`). This operation is applied to each number in the `nums` list.

---

### **7. Filtering and Mapping Together**
```python
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, nums)))
print(result)  # Output: [1, 9, 25]
```
**What the first `lambda` does**:  
The first `lambda` in the `filter` checks if a number `x` is odd (`x % 2 != 0`) and keeps only the odd numbers.  
**What the second `lambda` does**:  
The second `lambda` in the `map` takes each odd number and returns its square (`x**2`).

---

### **8. Custom Aggregation Using `reduce`**
```python
nums = [5, 2, 4]
max_val = reduce(lambda x, y: x if x > y else y, nums)
print(max_val)  # Output: 5
```
**What the `lambda` does**:  
The `lambda` takes two numbers, `x` and `y`, and returns the larger of the two (`x` if `x > y`, otherwise `y`). The `reduce` function uses this `lambda` to find the maximum value in the list.


You can **add lambda** to various built-in Python functions that accept a **key**, **predicate**, **callback**, or **custom function**. Here’s a list of commonly used functions that work well with lambda:

### **Functions that Accept Lambdas**:
1. **`sorted()`**:
   - **Purpose**: Sorts an iterable.
   - **Use Case**: You can provide a `lambda` to customize the sorting order.
   ```python
   data = [3, 1, 4, 1, 5, 9]
   sorted_data = sorted(data, key=lambda x: x % 3)
   print(sorted_data)  # Output: [3, 9, 1, 4, 1, 5]
   ```

2. **`map()`**:
   - **Purpose**: Applies a function to all items in an iterable.
   - **Use Case**: You can use `lambda` to define the function to apply.
   ```python
   nums = [1, 2, 3, 4]
   doubled = list(map(lambda x: x * 2, nums))
   print(doubled)  # Output: [2, 4, 6, 8]
   ```

3. **`filter()`**:
   - **Purpose**: Filters elements in an iterable by a condition.
   - **Use Case**: You can provide a `lambda` to define the condition.
   ```python
   nums = [1, 2, 3, 4, 5]
   odd_nums = list(filter(lambda x: x % 2 != 0, nums))
   print(odd_nums)  # Output: [1, 3, 5]
   ```

4. **`reduce()`**:
   - **Purpose**: Applies a function cumulatively to the elements of an iterable.
   - **Use Case**: You can use `lambda` to define the function that combines elements.
   ```python
   from functools import reduce
   nums = [1, 2, 3, 4]
   product = reduce(lambda x, y: x * y, nums)
   print(product)  # Output: 24
   ```

5. **`min()` / `max()`**:
   - **Purpose**: Finds the minimum or maximum element in an iterable.
   - **Use Case**: You can provide a `lambda` to define how the elements should be compared.
   ```python
   numbers = [3, 1, 4, 1, 5, 9]
   min_value = min(numbers, key=lambda x: x % 3)
   print(min_value)  # Output: 3
   ```

6. **`any()` / `all()`**:
   - **Purpose**: Checks if any/all elements in an iterable meet a condition.
   - **Use Case**: You can use `lambda` to define the condition.
   ```python
   nums = [1, 2, 3, 4, 5]
   has_even = any(lambda x: x % 2 == 0, nums)
   print(has_even)  # Output: True
   ```

7. **`zip()`**:
   - **Purpose**: Combines two or more iterables element-wise.
   - **Use Case**: You can use `lambda` inside a list comprehension to perform operations on the zipped pairs.
   ```python
   a = [1, 2, 3]
   b = [4, 5, 6]
   result = list(zip(a, b, key=lambda x: x[0] + x[1]))
   print(result)  # Output: [(1, 4), (2, 5), (3, 6)]
   ```

8. **`sum()`**:
   - **Purpose**: Calculates the sum of elements in an iterable.
   - **Use Case**: You can use `lambda` to specify how to reduce the elements.
   ```python
   nums = [1, 2, 3, 4]
   total = sum(nums, lambda x, y: x + y)
   print(total)  # Output: 10
   ```

9. **`set()`**:
   - **Purpose**: Creates a set from an iterable.
   - **Use Case**: You can use `lambda` in set comprehensions or to apply a transformation.
   ```python
   data = [1, 2, 3, 4, 1, 2]
   unique_squares = set(map(lambda x: x**2, data))
   print(unique_squares)  # Output: {1, 4, 9, 16}
   ```

10. **`zip_longest()`**:
   - **Purpose**: Combines two or more iterables element-wise, filling with a default value.
   - **Use Case**: You can use `lambda` in a list comprehension to transform zipped elements.
   ```python
   a = [1, 2, 3]
   b = [4, 5]
   from itertools import zip_longest
   result = list(zip_longest(a, b, fillvalue=0))
   print(result)  # Output: [(1, 4), (2, 5), (3, 0)]
   ```

---

### **Use Lambda for Key Customization**:
- Many Python functions like `sorted()`, `min()`, and `max()` take a `key` argument, which is perfect for using `lambda` when you need custom sorting, aggregation, or comparison logic.

---

### **Summary**:
- **Lambda** works **anywhere** you need a short, simple function:
  - **Sorting** (`sorted()`)
  - **Mapping** (`map()`)
  - **Filtering** (`filter()`)
  - **Reduction** (`reduce()`)
  - **Comparison** (`min()`, `max()`)
  - **Logical checks** (`any()`, `all()`)
  - **Pairwise combining** (`zip()`, `zip_longest()`)
  - **Summing** (`sum()`)

Using **lambda** effectively can greatly simplify your code, especially in **LeetCode** problems where concise and efficient solutions are key!
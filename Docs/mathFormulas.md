For LeetCode and other coding interviews, knowing some key mathematical formulas and concepts can be very helpful. Here's a list of essential formulas and concepts you should remember:

### Arithmetic and Algebra

1. **Basic Arithmetic**:

   - Addition, subtraction, multiplication, division
   - Properties: commutative, associative, distributive

2. **Sum of First \( n \) Natural Numbers**:
   \[
   \text{Sum} = \frac{n(n + 1)}{2}
   \]

3. **Sum of First \( n \) Squares**:
   \[
   \text{Sum} = \frac{n(n + 1)(2n + 1)}{6}
   \]

4. **Sum of First \( n \) Cubes**:
   \[
   \text{Sum} = \left(\frac{n(n + 1)}{2}\right)^2
   \]

### Combinatorics

5. **Permutations** (arrangements of \( n \) items):
   \[
   P(n, r) = \frac{n!}{(n - r)!}
   \]

6. **Combinations** (selection of \( r \) items from \( n \) items):
   \[
   C(n, r) = \binom{n}{r} = \frac{n!}{r!(n - r)!}
   \]

### Geometry

7. **Area of Basic Shapes**:

   - Triangle: \(\text{Area} = \frac{1}{2} \times \text{base} \times \text{height}\)
   - Rectangle: \(\text{Area} = \text{length} \times \text{width}\)
   - Circle: \(\text{Area} = \pi r^2\)

8. **Perimeter of Basic Shapes**:

   - Triangle: \(\text{Perimeter} = a + b + c\)
   - Rectangle: \(\text{Perimeter} = 2(\text{length} + \text{width})\)
   - Circle: \(\text{Perimeter} = 2\pi r\)

9. **Pythagorean Theorem**:
   \[
   a^2 + b^2 = c^2
   \]

### Number Theory

10. **Greatest Common Divisor (GCD)** (using Euclidean algorithm):
    \[
    \text{GCD}(a, b) = \text{GCD}(b, a \% b)
    \]

11. **Least Common Multiple (LCM)**:
    \[
    \text{LCM}(a, b) = \frac{|a \times b|}{\text{GCD}(a, b)}
    \]

### Sequences and Series

12. **Arithmetic Progression (AP)**:

    - \( n \)-th term: \( a_n = a + (n - 1)d \)
    - Sum of first \( n \) terms: \( S_n = \frac{n}{2} [2a + (n - 1)d] \)

13. **Geometric Progression (GP)**:
    - \( n \)-th term: \( a_n = ar^{n-1} \)
    - Sum of first \( n \) terms: \( S_n = a \frac{1 - r^n}{1 - r} \) (for \( r \neq 1 \))
    - Sum to infinity (for \( |r| < 1 \)): \( S = \frac{a}{1 - r} \)

### Logarithms and Exponents

14. **Basic Logarithm Properties**:

    - \( \log(ab) = \log(a) + \log(b) \)
    - \( \log\left(\frac{a}{b}\right) = \log(a) - \log(b) \)
    - \( \log(a^b) = b \log(a) \)

15. **Exponent Properties**:
    - \( a^m \times a^n = a^{m+n} \)
    - \( \left(a^m\right)^n = a^{mn} \)
    - \( a^{-n} = \frac{1}{a^n} \)

### Probability

16. **Basic Probability**:
    \[
    P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of outcomes}}
    \]

17. **Conditional Probability**:
    \[
    P(A|B) = \frac{P(A \cap B)}{P(B)}
    \]

18. **Bayes' Theorem**:
    \[
    P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}
    \]

### Algorithms

19. **Binary Search**:

    - Time Complexity: \( O(\log n) \)

20. **Sorting Algorithms** (Time Complexities):

    - Quick Sort: \( O(n \log n) \) average, \( O(n^2) \) worst
    - Merge Sort: \( O(n \log n) \)
    - Bubble Sort: \( O(n^2) \)
    - Insertion Sort: \( O(n^2) \)

21. **Graph Algorithms**:
    - Dijkstra's Algorithm: \( O(V^2) \) or \( O(E \log V) \) with priority queue
    - Breadth-First Search (BFS): \( O(V + E) \)
    - Depth-First Search (DFS): \( O(V + E) \)

### Data Structures

22. **Common Data Structure Operations**:
    - HashMap (Average Case): Insert/Search/Delete: \( O(1) \)
    - Binary Search Tree (Average Case): Insert/Search/Delete: \( O(\log n) \)

### Complexity Classes

23. **Big O Notations**:
    - Constant: \( O(1) \)
    - Logarithmic: \( O(\log n) \)
    - Linear: \( O(n) \)
    - Linearithmic: \( O(n \log n) \)
    - Quadratic: \( O(n^2) \)
    - Cubic: \( O(n^3) \)
    - Exponential: \( O(2^n) \)

### Miscellaneous

24. **Modular Arithmetic**:
    \[
    (a + b) \% m = [(a \% m) + (b \% m)] \% m
    \]
    \[
    (a \times b) \% m = [(a \% m) \times (b \% m)] \% m
    \]

### Trigonometry

25. **Basic Trigonometric Functions**:
    - Sine, Cosine, Tangent and their relationships
    - Pythagorean identities: \( \sin^2\theta + \cos^2\theta = 1 \)

Understanding and being able to apply these formulas can help you solve a wide range of problems on LeetCode and in coding interviews.

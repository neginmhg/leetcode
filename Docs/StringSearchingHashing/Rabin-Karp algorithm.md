The **Rabin-Karp algorithm** is a string-searching algorithm that uses hashing to find an exact match of a pattern in a text efficiently. Its main advantage is the ability to perform a rolling hash to avoid recomputing hash values repeatedly.

Here's how it works step by step:

1. Compute the hash of the pattern and the initial hash of the first window of text.
2. Slide the window one character at a time, updating the hash using a rolling hash technique.
3. When the hash of the current window matches the pattern's hash, perform a direct comparison to confirm the match (since hash collisions are possible).
4. Continue sliding until the end of the text is reached.

Here's an implementation in Python:

```python
def rabin_karp(text, pattern):
    """
    Uses the Rabin-Karp algorithm to find all occurrences of a pattern in a given text.

    Parameters:
    - text (str): The text in which to search for the pattern.
    - pattern (str): The pattern to search for.

    Returns:
    - list: A list of starting indices where the pattern is found in the text.
    """
    # Define base and a prime modulus for hashing
    base = 256
    prime = 101

    # Lengths of the pattern and text
    m = len(pattern)
    n = len(text)

    # Initialize hash values for pattern and text's first window
    pattern_hash = 0
    window_hash = 0

    # Power of base^(m-1) modulo prime for rolling hash
    h = 1
    for i in range(m - 1):
        h = (h * base) % prime

    # Compute initial hash values for pattern and text's first window
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        window_hash = (base * window_hash + ord(text[i])) % prime

    # List to store the starting indices of matches
    result = []

    # Slide the window over the text
    for i in range(n - m + 1):
        # Check if the hash values match
        if pattern_hash == window_hash:
            # Verify by checking the actual characters
            if text[i:i + m] == pattern:
                result.append(i)

        # Compute the hash for the next window
        if i < n - m:
            window_hash = (base * (window_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            # Ensure the hash is positive
            if window_hash < 0:
                window_hash += prime

    return result

# Example usage
text = "abracadabra"
pattern = "abra"
print(rabin_karp(text, pattern))  # Output: [0, 7]
```

### Explanation
1. **Hashing**:
   - The hash of a string is computed using the formula:
     \[
     hash = (base^{m-1} \times c_1 + base^{m-2} \times c_2 + \ldots + c_m) \mod prime
     \]
   - This ensures quick updates when sliding the window.

2. **Sliding Window**:
   - For each character added to the window, subtract the hash contribution of the outgoing character and add the incoming character's contribution.
   
3. **Collision Check**:
   - If the hashes match, the actual strings are compared to avoid false positives.

### Complexity
- **Time Complexity**:
  - Best case: \(O(n + m)\) (when there are no hash collisions).
  - Worst case: \(O(n \cdot m)\) (when hash collisions occur frequently).
- **Space Complexity**: \(O(1)\) (apart from the input).
A **Trie** (pronounced "try") is a specialized tree-like data structure used primarily for managing a dynamic set of strings where keys are usually strings. Here’s a detailed breakdown of what a Trie is, how it works, and its common applications:

## Great for word validation problem

### What is a Trie?

A Trie is a tree-like structure that stores strings in a way that allows for efficient insertion, deletion, and lookup operations. It’s also known as a prefix tree because it stores strings in a way that reflects their common prefixes.

### Structure of a Trie

- **Nodes:** Each node represents a state in the string. It contains:

  - **Children:** Links to child nodes representing the next character in the string.
  - **End of Word Flag:** Indicates whether a node represents the end of a valid string.

- **Root:** The starting point of the Trie; it doesn’t store any characters.

### Basic Operations

1. **Insertion:**
   To insert a word, start from the root and follow the nodes that represent each character of the word. If a node for a character doesn’t exist, create it. Mark the end of the word at the last character node.

   ```python
   class TrieNode:
       def __init__(self):
           self.children = {}
           self.is_end_of_word = False

   class Trie:
       def __init__(self):
           self.root = TrieNode()

       def insert(self, word):
           node = self.root
           for char in word:
               if char not in node.children:
                   node.children[char] = TrieNode()
               node = node.children[char]
           node.is_end_of_word = True
   ```

2. **Search:**
   To search for a word, traverse the nodes according to the characters in the word. If you reach the end of the word and the end-of-word flag is set, the word is present.

   ```python
   def search(self, word):
       node = self.root
       for char in word:
           if char not in node.children:
               return False
           node = node.children[char]
       return node.is_end_of_word
   ```

3. **Deletion:**
   To delete a word, traverse to the end of the word and remove the end-of-word flag. If the node has no children, remove it and backtrack to delete unnecessary nodes.

   ```python
   def delete(self, word):
       def _delete(node, word, index):
           if index == len(word):
               if not node.is_end_of_word:
                   return False
               node.is_end_of_word = False
               return len(node.children) == 0
           char = word[index]
           if char not in node.children:
               return False
           should_delete_child = _delete(node.children[char], word, index + 1)
           if should_delete_child:
               del node.children[char]
               return len(node.children) == 0
           return False

       _delete(self.root, word, 0)
   ```

4. **Prefix Search:**
   To find if there is any word in the Trie that starts with a given prefix, traverse the nodes following the prefix characters.

   ```python
   def starts_with(self, prefix):
       node = self.root
       for char in prefix:
           if char not in node.children:
               return False
           node = node.children[char]
       return True
   ```

### Advantages of Using a Trie

1. **Efficient Search Operations:** Trie allows for O(n) search complexity where n is the length of the string.
2. **Prefix Matching:** Efficiently supports prefix-based searches, which is useful in applications like autocomplete.
3. **Memory Efficiency:** Shares common prefixes between strings, which saves space compared to storing all strings independently.

### Applications of Tries

1. **Autocomplete and Spell Checking:** Used in search engines and text editors for suggesting completions and checking spelling.
2. **IP Routing:** Used in networking for efficient IP address lookup.
3. **Dictionary Implementations:** Used in word games and language dictionaries for quick lookup.

### Example Trie Implementation

Here’s a complete example of a Trie in Python:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        def _delete(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = word[index]
            if char not in node.children:
                return False
            should_delete_child = _delete(node.children[char], word, index + 1)
            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0
            return False

        _delete(self.root, word, 0)
```

Here’s a table summarizing everything you need to know about Tries for HackerRank and LeetCode problems:

| **Topic**                    | **Details**                                                                                     |
| ---------------------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------- |
| **Definition**               | A Trie is a tree-like data structure used for efficient retrieval of strings based on prefixes. |
| **Basic Operations**         | **Operation**                                                                                   | **Description**                                                                              | **Complexity**    |
| -------------------------    | ----------------                                                                                | ----------------------------------------                                                     | ----------------- |
| **Insertion**                | Insert a string into the Trie.                                                                  | O(n), where n is the length of the string.                                                   |
| **Search**                   | Check if a string is present in the Trie.                                                       | O(n), where n is the length of the string.                                                   |
| **Prefix Matching**          | Check if there are any strings with a given prefix.                                             | O(n), where n is the length of the prefix.                                                   |
| **Deletion**                 | Remove a string from the Trie.                                                                  | O(n), where n is the length of the string.                                                   |
| **Autocomplete**             | Find all words with a given prefix.                                                             | O(n + m), where n is the length of the prefix and m is the number of words with that prefix. |
| **Count Prefix Occurrences** | Count how many words have a given prefix.                                                       | O(n), where n is the length of the prefix.                                                   |

| **Common Problems**                                           | **Description**                                                         | **Strategy**                                                        |
| ------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **LeetCode 208: Implement Trie (Prefix Tree)**                | Implement Trie data structure.                                          | Implement basic operations: `insert`, `search`, `startsWith`.       |
| **LeetCode 211: Add and Search Word - Data structure design** | Design a data structure to add and search words.                        | Use a Trie with a method to handle both word and prefix queries.    |
| **LeetCode 212: Word Search II**                              | Find all words in a 2D board.                                           | Implement Trie and DFS to explore the board.                        |
| **LeetCode 421: Maximum XOR of Two Numbers in an Array**      | Find the maximum XOR of any two numbers.                                | Use a Trie to represent binary numbers and compute the maximum XOR. |
| **HackerRank: Contacts**                                      | Design a data structure for phone contacts.                             | Implement insert, search, and prefix matching methods.              |
| **LeetCode 784: Letter Case Permutation**                     | Find all permutations of a string with uppercase and lowercase letters. | Use backtracking and Trie to generate all possible combinations.    |
| **LeetCode 1268: Search Suggestions System**                  | Design a system for product suggestions based on user input.            | Use Trie to store products and generate suggestions.                |
| **LeetCode 1457: Pseudo-Palindromic Paths in a Binary Tree**  | Count paths that form pseudo-palindromes.                               | Use Trie for managing paths and counting pseudo-palindromic paths.  |

| **Advanced Features**    | **Description**                                                               |
| ------------------------ | ----------------------------------------------------------------------------- |
| **Suffix Trees**         | A data structure that represents all suffixes of a string.                    |
| **Radix Trees**          | A space-optimized variant of Trie where nodes with only one child are merged. |
| **Ternary Search Trees** | A variation of Trie that uses ternary search for more space efficiency.       |

| **Visualization and Debugging**        | **Method**                                                       |
| -------------------------------------- | ---------------------------------------------------------------- |
| **Print the Trie**                     | Add a method to print the Trie structure for visualization.      |
| **Graphviz for Visual Representation** | Use `graphviz` to create a graphical representation of the Trie. |

| **Sample Problems and Solutions** | **Solution**                                                       |
| --------------------------------- | ------------------------------------------------------------------ |
| **Implement Trie**                | Implement `insert`, `search`, `startsWith` methods.                |
| **Find Words with Prefix**        | Use DFS to collect all words with a given prefix.                  |
| **Count Words with Prefix**       | Traverse Trie to count occurrences of words with the given prefix. |

### Useful Links

- [LeetCode Trie Problems](https://leetcode.com/tag/trie/)
- [HackerRank Trie Problems](https://www.hackerrank.com/domains/tutorials/10-days-of-javascript/10-days-of-javascript-strings)
- [Graphviz](https://graphviz.gitlab.io/)

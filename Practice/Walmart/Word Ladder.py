"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = 
["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""
from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #Edge Case
        if endWord not in wordList:
            return 0
        #build the neighbor map/adjacency list
        nei=defaultdict(list)
        wordList.append(beginWord)
        # O(n) iteration over words
        for word in wordList:
            # O(m) loop over each character in the word
            for c in range(len(word)):
                # Pattern generation takes O(m) due to slicing
                pattern=word[:c]+"*"+word[c+1:] #These patterns act as "wildcards" to group words that differ by only one letter.
                nei[pattern].append(word)
        # At this point, the complexity of this preprocessing step is:
        # O(n * m^2) because:
        # - We iterate over n words.
        # - For each word, we loop m times to create patterns.
        # - Each pattern generation takes O(m) for string slicing and concatenation.

        #setup bfs
        #BFS to find shortest
        #Deque
        #Visit Set
        visit=set(beginWord)
        q = deque([beginWord])
        res=1
        while q:
            #Process Each Level of the BFS
            fixedSize = len(q)  # Capture the current size of the queue to not run into inf loop
            for i in range(fixedSize):
                word=q.popleft()
                if word == endWord:
                    return res
                for c in range(len(word)):  # O(m) loop over word length
                    pattern=word[:c]+"*"+word[c+1:]# Generate O(m) patterns
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            
            res+=1 #increase the res for each level of bfs
        return 0

#n is the number of words 
#m is the length of the word.
#Time  compelxity:  O(m^2 . n)
#For word[:c]+"*"+word[c+1:] : If the input were mutable (like a list of characters), replacing characters in place would only cost
    #O(1) per operation. However, because strings in Python are immutable, slicing and concatenation have higher costs, which must be accounted for.
    #We add time complexity for slicing because slicing a string in Python involves creating a new string. 
    # Unlike in-place operations, slicing is not free—it requires copying elements into a new memory space.



#Space compelxity:  O(m . n)

"""
When working with the Word Ladder problem using the BFS approach described,
here are the top points to remember:

### 1. **Breadth-First Search (BFS) for Shortest Path**
   - **Why BFS?** BFS is used because it explores all possible transformations level by level, 
   ensuring that the first time you reach the `endWord`, you've found the shortest transformation 
   sequence.
   - **Level-based Exploration**: BFS naturally handles shortest path problems by exploring 
   all words one step away from the current word before moving to words two steps away, and so on.

### 2. **Pattern-Based Neighbor Map (Adjacency List)**
   - **Pattern Definition**: Patterns are formed by replacing each letter of a word with a 
   wildcard (`*`). For example, "hot" generates the patterns `*ot`, `h*t`, and `ho*`.
   - **Neighbor Map**: An adjacency list (`nei` dictionary) is used where each pattern maps 
   to a list of words that match that pattern. This allows quick lookup of all possible 
   one-letter transformations for any word.
   - **Precomputation**: Patterns for all words are precomputed once and stored in the `nei` 
   dictionary, optimizing the BFS by avoiding repetitive pattern generation.

### 3. **Early Exit Condition**
   - **End Word Check**: The algorithm immediately returns `0` if the `endWord` is not in the 
   `wordList`, since it's impossible to form a valid transformation sequence.
   - **Early Termination**: As soon as the `endWord` is found during BFS, 
   the algorithm returns the current transformation length, ensuring the shortest sequence 
   is returned.

### 4. **Tracking Visited Words**
   - **Visited Set**: A `visited` set is used to keep track of words that have already been explored. This prevents revisiting nodes, which could cause infinite loops or redundant work, and helps ensure that each word is only processed once.
   - **Avoid Cycles**: By marking words as visited as soon as they are 
   added to the queue, the algorithm avoids processing the same word multiple times, 
   which improves efficiency.

### 5. **Efficiency Considerations**
   - **Queue for BFS**: The BFS uses a queue (`deque`) to efficiently pop elements from the 
   front and append new words at the back.
   - **Preprocessing Overhead**: Although constructing the neighbor map has an upfront cost, 
   it significantly reduces the time complexity during BFS by enabling quick lookups.

### 6. **Edge Cases**
   - **No Valid Sequence**: The algorithm correctly handles cases where no valid transformation 
   sequence exists by returning `0`.
   - **Single Transformation**: If `beginWord` is already one letter away from `endWord`, 
   the BFS will correctly return a sequence length of 2.

### 7. **Scalability**
   - **Word Length**: The approach works efficiently even for long words, 
   as it processes each word in `O(L * 26)` where `L` is the length of the word, and `26` is the number of possible character replacements.
   - **Large Word Lists**: While the method scales well with larger word lists, 
   using techniques like Bidirectional BFS can further improve performance in very large datasets.

### Summary
- **BFS** ensures the shortest path.(queue)
- **Pattern-based neighbor map** enables efficient lookup of valid transformations.
- **Visited set** prevents cycles and redundant processing.
- **Precompute patterns** to optimize BFS execution.
- **Return early** if the end word is found or unreachable.

Remembering these points will help you understand and implement the solution efficiently, especially in scenarios involving shortest path problems in unweighted graphs like this one.
"""
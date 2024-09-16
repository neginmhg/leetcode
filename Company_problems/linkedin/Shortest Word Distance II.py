"""
You are given a list of words (`wordsDict`) and a list of pairs of words (`word1`, `word2`). For each pair, you need to find the shortest distance between the two words in the `wordsDict` list.

**Example:**
wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"

- For the pair ("coding", "practice"), the shortest distance is 3.

**Requirements:**
1. Implement a class `WordDistance` that has two methods:
   - **Constructor (`__init__`):** Initializes the `WordDistance` class with a list of words (`wordsDict`).

   - **`shortest` method:** Takes two words (`word1` and `word2`) as arguments and returns the shortest distance between the two words in the `wordsDict`.

**Constraints:**
- The list `wordsDict` contains at least 2 words and at most (10^4) words.
- Each word in `wordsDict` is a non-empty string.
- `word1` and `word2` are different words and will always appear at least once in `wordsDict`.

### Example Usage:
# Initialize with wordsDict
wd = WordDistance(["practice", "makes", "perfect", "coding", "makes"])

# Find shortest distance
print(wd.shortest("coding", "practice"))  # Output: 3
print(wd.shortest("makes", "coding"))     # Output: 1

You can use this class to efficiently query the shortest distance between any two words from the list.
"""
from typing import List
from collections import defaultdict
class WordDistance:
    def __init__(self, wordsDict:List[str]):
        self.wordsDict=wordsDict
        self.indexMap=defaultdict(list) #{"a":[2,4,8]}
        #populate a helper map
        for i,w in enumerate(wordsDict): #O(n)
            self.indexMap[w].append(i)
    def shortest(self, s1:str, s2:str)-> int:
        indexList1=self.indexMap[s1] 
        indexList2=self.indexMap[s2]
        #use 2 pointers to find the closest indexes
        i,j=0,0
        minDis=float("inf")
        #O(m + k): m length of indexList1 , k length of indexList2
        while i<len(indexList1) and j<len(indexList2):
            minDis=min(minDis, abs(indexList1[i]- indexList2[j]))
            #move pointers but how? find the 2 closest
            if (indexList1[i]< indexList2[j]):
                i+=1
            else:
                j+=1
        return minDis

#Time Complexity:
    #Initialization: O(n)
    #Shortest Distance Calculation: O(m + k)
    #TOTAL = O(n + m + k)

#Space Complexity: 
    #O(n)
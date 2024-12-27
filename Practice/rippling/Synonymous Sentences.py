"""
You are given a list of equivalent string pairs synonyms where synonyms[i] = [si, ti] indicates that si and ti are equivalent strings. You are also given a sentence text.

Return all possible synonymous sentences sorted lexicographically.

 

Example 1:

Input: synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am happy today but was sad yesterday"
Output: ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]
Example 2:

Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
 

Constraints:

0 <= synonyms.length <= 10
synonyms[i].length == 2
1 <= si.length, ti.length <= 10
si != ti
text consists of at most 10 words.
All the pairs of synonyms are unique.
The words of text are separated by single spaces.
"""
from typing import List
import collections
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        #Using parent focuses purely on grouping relationships.
        #Creating choices transforms these relationships into a format suitable for backtracking.
        parent= {}      # synonym : representative
        #Union Find functions
        def find(x):
            if parent[x] != x:
                parent[x] =find(parent[x])
            return parent[x]

        def union(x,y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootY]=rootX
        
        #1. Union to group synonyms
        for s1, s2 in synonyms:
            if s1 not in parent:
                parent[s1] =s1
            if s2 not in parent:
                parent[s2]=s2
            print(parent,s1,s2)
            union(s1,s2)
            print(parent)
            print("\n")
        

        #2. Find the representation - Build synonym groups
        choices = collections.defaultdict(set)
        # {repStr : {str1, str2,...}}
        for word in parent:
            root = find(word)
            choices[root].add(word)
        


        #3. Parse sentence to words
        words =text.split()

        result =[]
        #4. Backtracking
        def backtrack(start, path):
            #base case
            if start ==len(words):
                result.append(" ".join(path))
                return
            #for loop to explore choices
            curWord=words[start]
            if curWord in parent: #if word has synonym
                root =find(curWord)
                for syn in sorted(choices[root]):
                    backtrack(start+1, path +[syn])
            else:
                backtrack(start+1, path + [curWord])
        
        backtrack(0,[])
        return result



s = Solution()
synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
text = "I am happy today but was sad yesterday"
out = s.generateSentences(synonyms, text)
#print(out)
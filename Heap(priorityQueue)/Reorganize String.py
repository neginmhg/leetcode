"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.


"""
from typing import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        prev=None
        heap = [[-count,char] for char,count in freq.items()]
        heapq.heapify(heap)         # [[2,a], [1,b]]
        res =""
        while heap :
            count,char = heapq.heappop(heap)
            count+=1
            res +=char
            if prev:  # If there's a previously used character, push it back to the heap
                heapq.heappush(heap, prev)
            
            # If there are still more of the current character, save it as prev
            if count < 0:
                prev = [count, char]
            else:
                prev = None  # No more of the current character, reset prev
        
        # Step 4: If the length of the result is equal to the length of the input, return it
        return res if len(res) == len(s) else ""

s = Solution()
res=s.reorganizeString("aab")
print(res)
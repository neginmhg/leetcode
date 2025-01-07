""" [HARD]
You are given a string s consisting only of lowercase English letters.

In one move, you can select any two adjacent characters of s and swap them.

Return the minimum number of moves needed to make s a palindrome.

Note that the input will be generated such that s can always be converted to a palindrome.

 

Example 1:

Input: s = "aabb"
Output: 2
Explanation:
We can obtain two palindromes from s, "abba" and "baab". 
- We can obtain "abba" from s in 2 moves: "aabb" -> "abab" -> "abba".
- We can obtain "baab" from s in 2 moves: "aabb" -> "abab" -> "baab".
Thus, the minimum number of moves needed to make s a palindrome is 2.
Example 2:

Input: s = "letelt"
Output: 2
Explanation:
One of the palindromes we can obtain from s in 2 moves is "lettel".
One of the ways we can obtain it is "letelt" -> "letetl" -> "lettel".
Other palindromes such as "tleelt" can also be obtained in 2 moves.
It can be shown that it is not possible to obtain a palindrome in less than 2 moves.
 
"""
#https://www.youtube.com/watch?v=2Vcdjb-H8yA
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        listS = list(s)
        res =0
        while listS:
            last = listS[-1]
            #index of duplicate of last
            i = listS.index(last)

            #if i is the last index
            #means there was 1 existing element
            if i==len(listS)-1:
                res += i//2
            else:
                res +=i
                listS.pop(i)
            listS.pop()
        return res

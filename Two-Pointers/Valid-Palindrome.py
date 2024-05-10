""" [EASY]
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #filter useless characters
        #lower case the string
        #reverse the string and check if it's as same as the original
        newStr=""
        for c in s:
            if c.isalnum():         #isalnum checks for alphabet chars
                newStr +=c.lower()
        print(newStr,newStr[::-1]) #amanaplanacanalpanama    ,    amanaplanacanalpanama
        return newStr==newStr[::-1]     #str[::-1] reverses a string
    
    def isPalindrome2(self, s: str) -> bool:
        l, r =0, len(s)-1               #setup L and R
        while l<r:
           while l<r and not self.isalnum2(s[l]):
               l+=1
           while l<r and not self.isalnum2(s[r]):
               r-=1
           if s[l].lower()!=s[r].lower():
               return False
           l, r= l+1, r-1
        return True

    def isalnum2(self,c):
        return (ord('A')<=ord(c)<=ord('Z') or
                ord('a')<=ord(c)<=ord('z') or
                ord('0')<=ord(c)<=ord('9'))
    
s=Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama")) #True

print(s.isPalindrome2("A man, a plan, a canal: Panama")) #True


"""
lessons learnt:
- To reverse a string(str) do -->           str[::-1]
- To check if a char is alphabet do -->     c.isalnum()
- To get ASCII value of a char do -->        ord(char)
- To make sure a char is not a special char do -->
        ord('A')<=ord(c)<=ord('Z') 
        ord('a')<=ord(c)<=ord('z') 
        ord('0')<=ord(c)<=ord('9')

"""
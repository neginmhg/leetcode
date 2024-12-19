""""

The "Cipher Problem" is a common algorithmic challenge that involves encoding and decoding messages using various cipher techniques. One such technique is the Caesar cipher, which shifts each letter in the plaintext by a fixed number of positions down or up the alphabet.

Problem Statement:

You are given a string s representing a message and an integer k representing the shift value. Your task is to encode the message using the Caesar cipher technique, shifting each letter in the string by k positions down the alphabet.

Example:
s = "abc"
k = 3
encoded_message = caesar_cipher(s, k)
print(encoded_message)  # Output: "def"

Approach:

To implement the Caesar cipher:

Normalize the Shift: Since the alphabet has 26 letters, a shift of k is equivalent to a shift of k % 26. This ensures that shifts larger than 26 wrap around the alphabet.
Iterate Through the String: For each character in the string:
If the character is a lowercase letter ('a' to 'z'), shift it within the lowercase letters.
If the character is an uppercase letter ('A' to 'Z'), shift it within the uppercase letters.
If the character is not a letter, leave it unchanged.
Construct the Encoded Message: Combine the shifted characters to form the encoded message.
"""

class Solurion:
    def caesar_cipher(s: str, k: int) -> str:
        k = k % 26  # Normalize the shift to be within 0-25
        result = []

        for char in s:
            if 'a' <= char <= 'z':
                # Shift within lowercase letters
                new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
                result.append(new_char)
            elif 'A' <= char <= 'Z':
                # Shift within uppercase letters
                new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
                result.append(new_char)
            else:
                # Non-alphabetic characters remain unchanged
                result.append(char)

        return ''.join(result)
    
"""For example, if char = 'Z' and k = 3, 
ord('Z') - ord('A') + k = 25 + 3 = 28, but 28 % 26 = 2, 
which corresponds to the letter 'C'."""
#Time Complexity: O(n), where n is the length of the 
# input string s. Each character is processed once.

#Space Complexity: O(n), as the result is stored in a 
# list of the same length as the input string.
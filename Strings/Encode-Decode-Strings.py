"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
# Test Case 1
strs = ["Hello", "World"]
encoded_str = codec.encode(strs)
decoded_strs = codec.decode(encoded_str)
assert decoded_strs == strs, f"Test Case 1 Failed: Expected {strs}, but got {decoded_strs}"

# Test Case 2
strs = ["LeetCode", "is", "awesome!"]
encoded_str = codec.encode(strs)
decoded_strs = codec.decode(encoded_str)
assert decoded_strs == strs, f"Test Case 2 Failed: Expected {strs}, but got {decoded_strs}"

# Test Case 3
strs = []
encoded_str = codec.encode(strs)
decoded_strs = codec.decode(encoded_str)
assert decoded_strs == strs, f"Test Case 3 Failed: Expected {strs}, but got {decoded_strs}"

# Test Case 4
strs = ["a"]
encoded_str = codec.encode(strs)
decoded_strs = codec.decode(encoded_str)
assert decoded_strs == strs, f"Test Case 4 Failed: Expected {strs}, but got {decoded_strs}"

# Test Case 5
strs = ["aaa", "bb", "c"]
encoded_str = codec.encode(strs)
decoded_strs = codec.decode(encoded_str)
assert decoded_strs == strs, f"Test Case 5 Failed: Expected {strs}, but got {decoded_strs}"


1. `encode`: Given a list of strings, encode them into a single string.
2. `decode`: Given an encoded string, decode it to the original list of strings.

Here's how you can approach solving this problem:

### Approach:

#### Encoding:

For encoding, you can use a delimiter to separate individual strings. One approach is to use the length of each string as a prefix before the actual string content. This way, you can determine where each string ends when decoding.

#### Decoding:

When decoding, you can iterate through the encoded string, extract each string's length, and then extract the actual string content using that length.

### Python Solution:

"""
class Solution:
    
    def encode(self, strs):
        encoded_str = [] #list of encoded strings
        for s in strs:
            # Encode each string as <length><delimiter><string>
            encoded_str.append(str(len(s)) + '/' + s)
        print(encoded_str) #['3/aaa', '2/bb', '1/c']
        return ''.join(encoded_str) # turn list of strings into 1 sting
    
    def decode(self, s):
        decoded = []
        i = 0
        while i < len(s):
            # Find delimiter
            delimiter_index = s.find('/', i)
            # Extract length of the string
            length = int(s[i:delimiter_index])
            # Extract string content
            decoded.append(s[delimiter_index + 1:delimiter_index + 1 + length])
            # Move to the next string
            i = delimiter_index + 1 + length
        return decoded
"""
### Explanation:

- In the `encode` method, we iterate through each string in the list `strs`. We prepend the length of the string followed by a delimiter (`/`) to each string and append it to the `encoded` list.
  
- In the `decode` method, we iterate through the encoded string `s`. We find the delimiter `/` to determine the length of the next string. Then we extract the string content based on that length and append it to the `decoded` list.

### Tricks:

1. **Delimiter**: Using a delimiter helps distinguish between the lengths and actual string content.
2. **String Length Prefix**: Prepending the length of each string before the actual string makes it easier to decode.

This approach ensures that you can encode and decode the list of strings without any loss of information. It uses the length of each string as metadata to separate and decode the strings correctly."""

s=Solution()
sampleList=["aaa", "bb", "c"]
result_encoded=s.encode(sampleList)
print(result_encoded) #3/aaa2/bb1/c
result_decoded=s.decode(result_encoded)
print(result_decoded) #['aaa', 'bb', 'c']
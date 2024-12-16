"""
Design a data structure that supports the following operations:

add: Add a number to an internal data structure.
find: Find if there exists any pair of numbers whose sum is equal to a specific target value.
Implement the TwoSum class:

TwoSum(): Initializes the TwoSum object.
void add(int number): Adds the integer number to the data structure.
bool find(int value): Returns true if there exists any pair of numbers whose sum is equal to value, otherwise it returns false.

Constraints:
You can assume that all input values are integers.
At most 10^4 calls will be made to the add and find methods.

# Initialize the TwoSum object
twoSum = TwoSum()

# Add numbers to the data structure
twoSum.add(1)      # Adding 1
twoSum.add(3)      # Adding 3
twoSum.add(5)      # Adding 5

# Find if a pair with sum equal to the target exists
twoSum.find(4)     # Returns True (1 + 3 = 4)
twoSum.find(7)     # Returns False (no pairs sum to 7)
"""
#to be able to use 2 pointers, we need to sort the array everytime calling find
#this is because we are not adding values in order.
#so, use dictionary
from collections import defaultdict
class TwoSum:
    def __init__(self):
        # Initialize the data structure
        self.numCount=defaultdict(int) #{1:2,3:1,5:1} number:count
    
    def add(self, number: int) -> None:
        # Add a number to the data structure
        self.numCount[number]+=1
    
    def find(self, value: int) -> bool:
        # Find if there exists any pair whose sum equals value
        for n in self.numCount:
            target=value-n
            # Case 1: If target is the same as n, check if there are at least 2 occurrences
            if target == n and self.numCount[n] > 1:
                return True
            # Case 2: If target is different, check if it exists in the map
            elif target != n and target in self.numCount:
                return True
        return False
           
#If we consider the entire TwoSum data structure:
#Time Complexity: 
    #The add operation is O(1), and the find operation is O(m), making the overall complexity dynamic based on the number of calls.
#Space Complexity: 
    # O(n) for storing unique numbers.
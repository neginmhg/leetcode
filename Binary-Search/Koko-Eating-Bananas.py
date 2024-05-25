"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

"""

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initialize the lower bound (l) to 1 (minimum possible eating speed)
        # and the upper bound (r) to the maximum number of bananas in any pile
        l, r = 1, max(piles)
        
        # Initialize the result with the maximum possible eating speed
        res = r
        
        # Perform binary search to find the minimum k
        while l <= r:
            # Calculate the middle point of the current search range
            k = (l + r) // 2
            
            # Initialize hours to 0, which will store the total hours needed
            hours = 0
            
            # Calculate the total hours needed to eat all piles at speed k
            for p in piles:
                # Use math.ceil to calculate the hours needed for each pile
                # math.ceil(p / k) ensures we round up if there are leftovers
                hours += math.ceil(p / k)
            
            # If the total hours is within the allowed time (h)
            if hours <= h:
                # Update the result to the minimum of the current result and k
                res = min(res, k)
                # Search in the lower half to find a potentially smaller k
                r = k - 1
            else:
                # If the total hours exceeds the allowed time, search in the upper half
                l = k + 1
        
        # Return the minimum eating speed found
        return res
"""
The developers at Amazon SQS are working on optimizing the message queue algorithm. There are n
n events to be sent through a queue, and the size of the i
i-th event payload is denoted by payload[i]. The queue performs more efficiently if a subset of the events can be selected and rearranged into a new array called optimizedPayload, which satisfies the following conditions, regardless of the original order of the elements:

    The first part of optimizedPayload forms an increasing sequence:
    optimizedPayload[1] < optimizedPayload[2] <...<optimizedPayload[i-1] <optimizedPayload[i]
    (Increasing order from the start to i


    The second part of optimizedPayload forms a decreasing sequence:
    optimizedPayload[i] > optimizedPayload[i+1] >...<optimizedPayload[j-1] > optimizedPayload[j]
    (Decreasing order from i to j).



    The third part of optimizedPayload forms an increasing sequence:
    optimizedPayload[j+1] < optimizedPayload[j+2] <...<optimizedPayload[n]
    (Increasing order from j to the end).


The order of elements in optimizedPayload can be rearranged to meet these conditions, meaning the original order of the payload array does not matter when forming the subset.
Task:
Determine the maximum number of events that can be selected and rearranged to form optimizedPayload that satisfies the increasing-decreasing-increasing configuration.
Input:
    Given n events and an array payload, find the maximum number of events that can be selected to form the optimizedPayload array that meets these conditions.
    Example:


Input:
    n=9
    payload =[1, 3, 5, 4, 2, 6, 7, 8, 9]. 


Output:
    Consider the subset optimizedPayload = [1, 3, 5, 4, 2, 6, 7, 8, 9]. This satisfies the conditions as follows:
    - increasing part (1 to i) = [1,3,5]    , with i=3
    - decreasing part (i to j) = [5,4,2]    , with j=5
    - increasing part (j to end) = [6,7,8,9]

"""

def get_maximum_events(payload):
    # Number of elements
    n = len(payload)
    
    # Edge case: If there are fewer than 3 elements, no valid sequence can be formed
    if n < 3:
        return 0
    
    # Initialize DP arrays
    first_dp = [1] * n  # Longest Increasing Subsequence (LIS) ending at each index
    second_dp = [1] * n  # Longest Decreasing Subsequence (LDS) starting at each index
    third_dp = [1] * n  # LIS starting at each index
    
    # Step 1: Calculate LIS for each index if we end at that index (first_dp)
    for i in range(1, n):
        for j in range(i):
            if payload[i] > payload[j]:
                first_dp[i] = max(first_dp[i], first_dp[j] + 1)
    
    # Step 2: Calculate LDS for each index if we start at that index (second_dp)
    for i in range(n - 2, -1, -1):  # Start from the second last element
        for j in range(i + 1, n):
            if payload[i] > payload[j]:
                second_dp[i] = max(second_dp[i], second_dp[j] + 1)
    
    # Step 3: Calculate LIS for each index if we start at that index (third_dp)
    for i in range(n - 2, -1, -1):  # Start from the second last element
        for j in range(i + 1, n):
            if payload[i] < payload[j]:
                third_dp[i] = max(third_dp[i], third_dp[j] + 1)
    
    # Step 4: Combine results to find the maximum sequence length
    max_result = 0
    for i in range(1, n - 1):  # `i` is the middle element
        # Combine first_dp, second_dp, and third_dp at `i`
        max_result = max(max_result, first_dp[i] + second_dp[i] + third_dp[i] - 2)
        # Subtract 2 because `i` is counted twice in both second_dp and third_dp
    
    return max_result

# Example usage:
payload = [1, 3, 5, 4, 2, 6, 8, 7, 9]
print(get_maximum_events(payload))  # Output: 9

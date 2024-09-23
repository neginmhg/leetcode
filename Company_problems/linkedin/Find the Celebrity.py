"""
Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) that tells you whether a knows b. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.

Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.

 

Example 1:


Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
Example 2:


Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.
 

Constraints:

n == graph.length == graph[i].length
2 <= n <= 100
graph[i][j] is 0 or 1.
graph[i][i] == 1
 

Follow up: If the maximum number of allowed calls to the API knows is 3 * n, could you find a solution without exceeding the maximum number of calls?

"""
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0 #choose a candidate
    
        # Step 1: Identify a potential celebrity
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i  # candidate cannot be celebrity if they know someone
        
        # Step 2: Verify the candidate
        for i in range(n):
            if i != candidate:
                if knows(candidate, i) or not knows(i, candidate):
                    return -1  # candidate knows someone or someone doesn't know candidate
                    
        return candidate  # Candidate is a celebrity

#Key Algorithmic Techniques:
#Greedy Approach: In the first phase, we greedily eliminate non-celebrities as soon as we find out they know someone.
#Single Candidate: The algorithm narrows down to one potential celebrity in O(n) time, instead of comparing every pair.
#Verification: The second phase verifies if the candidate actually satisfies both conditions of being a celebrity.
#In summary, the algorithm is an efficient two-phase approach using greedy elimination and verification, which ensures the solution is optimal in terms of function calls.


#Since both the candidate identification and verification phases take O(n) time, the total time complexity is O(2n), which is linear in terms of the number of people.
#This makes it efficient and ensures that we stay within the 3 * n limit of knows() function calls.
"""
Question 1

Suppose we have an unsorted log file of accesses to web resources. Each log entry consists of an access time, the ID of the user making the access, and the resource ID. The access time is represented as seconds since 00:00:00, and all times are assumed to be in the same day. For example:

logs1 = [
["58523", "user_1", "resource_1"],
["62314", "user_2", "resource_2"],
["54001", "user_1", "resource_3"],
["200", "user_6", "resource_5"],
["215", "user_6", "resource_4"],
["54060", "user_2", "resource_3"],
["53760", "user_3", "resource_3"],
["58522", "user_22", "resource_1"],
["53651", "user_5", "resource_3"],
["2", "user_6", "resource_1"],
["100", "user_6", "resource_6"],
["400", "user_7", "resource_2"],
["100", "user_8", "resource_6"],
["54359", "user_1", "resource_3"],
]
Example 2:

logs2 = [
["300", "user_1", "resource_3"],
["599", "user_1", "resource_3"],
["900", "user_1", "resource_3"],
["1199", "user_1", "resource_3"],
["1200", "user_1", "resource_3"],
["1201", "user_1", "resource_3"],
["1202", "user_1", "resource_3"]
]
Write a function that takes the logs and returns each users min and max access timestamp Example Output:

user_3:[53760,53760]
user_2:[54060,62314]
user_1:[54001,58523]
user_7:[400,400]
user_6:[2,215]
user_5:[53651,53651]
user_4:[58522,58522]
user_8:[100,100]
Question 2

Write a function that takes the logs and returns the resource with the highest number of accesses in any 5 minute window, together with how many accesses it saw.

Expected Output:

most_requested_resource(logs1) # => ('resource_3', 3)
Reason: resourc‍‍‍‍‍‍‌‌‌‌‌‍‌‍‍‌‌‍‍e_3 is accessed at 53760, 54001, and 54060

Question 3

Write a function that takes the logs as input, builds the transition graph and returns it as an adjacency list with probabilities. Add START and END states.

Specifically, for each resource, we want to compute a list of every possible next step taken by any user, together with the corresponding probabilities. The list of resources should include START but not END, since by definition END is a terminal state.

Expected output for logs1:

transition_graph(logs1) # =>
{{
'START': {'resource_1': 0.25, 'resource_2': 0.125, 'resource_3': 0.5, 'resource_6': 0.125},
'resource_1': {'resource_6': 0.333, 'END': 0.667},
'resource_2': {'END': 1.0},
'resource_3': {'END': 0.4, 'resource_1': 0.2, 'resource_2': 0.2, 'resource_3': 0.2},
'resource_4': {'END': 1.0},
'resource_5': {'resource_4': 1.0},
'resource_6': {'END': 0.5, 'resource_5': 0.5}
}}
For example, of 8 total users, 4 users have resource_3 as a first visit (user_1, user_2, user_3, user_5), 2 users have resource_1 as a first visit (user_6, user_22), 1 user has resource_2 as a first visit (user_7), and 1 user has resource_6 (user_8) so the possible next steps for START are resource_3 with probability 4/8, resource_1 with probability 2/8, and resource_2 and resource_6 with probability 1/8.For example, of 8 total users, 4 users have resource_3 as a first visit (user_1, user_2, user_3, user_5), 2 users have resource_1 as a first visit (user_6, user_22), 1 user has resource_2 as a first visit (user_7), and 1 user has resource_6 (user_8) so the possible next steps for START are resource_3 with probability 4/8, resource_1 with probability 2/8, and resource_2 and resource_6 with probability 1/8. These are the resource paths per user for the first logs example, ordered by access time:

{{
'user_1': ['resource_3', 'resource_3', 'resource_1'],
'user_2': ['resource_3', 'resource_2'],
'user_3': ['resource_3'],
'user_5': ['resource_3'],
'user_6': ['resource_1', 'resource_6', 'resource_5', 'resource_4'],
'user_7': ['resource_2'],
'user_8': ['resource_6'],
'user_22': ['resource_1'],

Expected output for logs2:
transition_graph(logs2) # =>
'START': {'resource_3': 1.0},
'resource_3': {'resource_3: 0.857, 'END': 0.143}
}
"""

from collections import defaultdict
class Solution:
    def userAcessTime(self, logs):
        userTimesDict = defaultdict(list)

        for log in logs:
            timestamp, userId, resourceId = log
            userTimesDict[userId].append(int(timestamp))
        
        result ={}
        for userId, times in userTimesDict.items():
            result[userId]= [min(times),max(times)]
        

        return result
    

    def mostRequestedResource(logs):
        resourceDict = defaultdict(list)
        for log in logs:
            timestamp, userId, resourceId = log
            resourceDict[resourceId].append(timestamp)
        

        maxAccess=0
        mostRequested = None

        for resource, times in resourceDict.items():
            times.sort()
            for i in range(len(times)):
                count=1 
                for j in range(i+1, len(times)):
                    if times[j]-times[i] <=300:
                        coutn+=1

                    else:
                        break
            
                if count>maxAccess:
                    maxAccess=count
                    mostRequested = resource
        
        return mostRequested,maxAccess
    
    def transition_graph(logs):
        user_paths = defaultdict(list)
        for log in sorted(logs, key=lambda x: (x[1], int(x[0]))):
            _, user_id, resource = log
            user_paths[user_id].append(resource)
        
        transitions = defaultdict(Counter)
        for user, path in user_paths.items():
            transitions['START'][path[0]] += 1
            for i in range(len(path) - 1):
                transitions[path[i]][path[i + 1]] += 1
            transitions[path[-1]]['END'] += 1
        
        transition_probabilities = {}
        for state, next_states in transitions.items():
            total = sum(next_states.values())
            transition_probabilities[state] = {k: v / total for k, v in next_states.items()}
        
        return transition_probabilities
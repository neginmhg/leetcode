"""
You are given an array of currency conversion rates, where each rate is represented as a triplet [currency1, currency2, rate]. This indicates that 1 unit of currency1 is equal to rate units of currency2. The conversion rates form a connected graph.

You are also given a query in the form of ['from', 'to'], asking you to calculate the conversion rate from the 'from' currency to the 'to' currency. If no conversion is possible, return -1.

Input:
[    ['USD', 'JPY', 110],
    ['USD', 'AUD', 1.45],
    ['JPY', 'GBP', 0.0070]
]

Query:
['GBP', 'AUD']


Output:
1.89

Explanation: GBP -> JPY -> USD -> AUD

"""
from collections import defaultdict, deque
from typing import List

class Solution:
    def currencyConversion(self, rates: List[List], query: List[str]) -> float:
        # Step 1: Build the graph
        graph = defaultdict(list)
        for currency1, currency2, rate in rates:
            graph[currency1].append((currency2, rate))
            graph[currency2].append((currency1, 1 / rate))  # Add reverse conversion

        # Step 2: Perform BFS to find the conversion rate
        start, end = query
        if start not in graph or end not in graph:
            return -1.0  # Return -1 if either currency is not in the graph
        
        # BFS initialization
        queue = deque([(start, 1.0)])  # (current_currency, cumulative_rate)
        visited = set()

        while queue:
            current_currency, cumulative_rate = queue.popleft()
            if current_currency == end:
                return cumulative_rate  # Return the conversion rate if we reach the target

            visited.add(current_currency)
            
            for neighbor, rate in graph[current_currency]:
                if neighbor not in visited:
                    queue.append((neighbor, cumulative_rate * rate))

        return -1.0  # Return -1 if no path exists between 'from' and 'to'

# Example usage
rates = [
    ['USD', 'JPY', 110],
    ['USD', 'AUD', 1.45],
    ['JPY', 'GBP', 0.0070]
]
query = ['GBP', 'AUD']

solution = Solution()
result = solution.currencyConversion(rates, query)
print(result)  # Output: 1.89

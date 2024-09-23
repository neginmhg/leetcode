To master **greedy algorithms** for solving Leetcode problems, it's essential to understand the key concepts, common problem patterns, and strategies to identify when a greedy solution is applicable. Here’s a comprehensive guide to everything you need to know:

### 1. **What is a Greedy Algorithm?**

A greedy algorithm builds a solution piece by piece, making the **locally optimal choice** at each step with the hope that this leads to a globally optimal solution. Unlike dynamic programming, it doesn’t backtrack or make multiple decisions at each step.

### 2. **Greedy Algorithm Properties**

For a greedy algorithm to work, the problem must satisfy the following two properties:

- **Greedy Choice Property**: A locally optimal choice will lead to a globally optimal solution.
- **Optimal Substructure**: The problem can be broken down into smaller subproblems, and an optimal solution to the subproblems can be used to solve the overall problem.

### 3. **How to Identify if Greedy Works**

Greedy algorithms usually work well in problems that ask for:

- **Maximum** or **minimum** results (e.g., maximum profit, minimum cost).
- **Optimization problems** (e.g., minimizing time, maximizing value).
- Problems where **decisions** can be made without reconsideration.

Key to solving problems with a greedy approach is recognizing that the **local decision** made at each step **does not impact future decisions negatively**.

### 4. **Common Problem Patterns for Greedy Algorithms**

1. **Interval Problems**

   - Problems that involve selecting intervals with the least overlap.
   - **Example**: Activity selection, meeting rooms.
   - **Strategy**: Sort the intervals and always choose the next activity that ends the earliest and doesn't overlap.

   ```python
   def activity_selection(activities):
       activities.sort(key=lambda x: x[1])  # Sort by end time
       last_end_time = 0
       selected = 0
       for start, end in activities:
           if start >= last_end_time:
               selected += 1
               last_end_time = end
       return selected
   ```

2. **Greedy for Profit/Maximization**

   - Problems where you need to maximize something (e.g., profit, number of tasks).
   - **Example**: Fractional knapsack problem.
   - **Strategy**: Sort by profit-to-cost ratio or value-to-weight ratio and greedily choose the best option.

   ```python
   def fractional_knapsack(values, weights, capacity):
       items = sorted(zip(values, weights), key=lambda x: x[0] / x[1], reverse=True)
       total_value = 0
       for value, weight in items:
           if capacity - weight >= 0:
               total_value += value
               capacity -= weight
           else:
               total_value += value * (capacity / weight)
               break
       return total_value
   ```

3. **Graph Problems**

   - Problems where you need to traverse a graph while optimizing a metric (e.g., shortest path, minimum spanning tree).
   - **Examples**: Dijkstra’s algorithm, Prim’s algorithm.
   - **Strategy**: Use priority queues to always pick the node with the shortest distance or minimum edge weight.

4. **Scheduling Problems**

   - Problems where you need to allocate resources to tasks, minimizing or maximizing some metric.
   - **Example**: Job scheduling, task scheduling.
   - **Strategy**: Greedily choose tasks based on deadlines, start times, or profit, depending on the problem.

5. **Partitioning Problems**
   - Problems where you need to split or partition data into groups in the most optimal way.
   - **Example**: Partition labels (Leetcode 763).
   - **Strategy**: Use sorting or scanning techniques to partition based on some criteria.

### 5. **Common Greedy Techniques**

- **Sorting**: Most greedy problems require you to sort the data in some specific order (e.g., by end time, by ratio, by deadline).
- **Priority Queues**: Often, greedy algorithms use priority queues to always get the current "best" option efficiently.
- **Choosing Locally Optimal Choices**: At each step, make the choice that seems best at the moment.

### 6. **Greedy vs Dynamic Programming**

- **Greedy**: Makes the best decision at each step and moves forward. Greedy is faster but doesn’t guarantee an optimal solution in all cases.
- **Dynamic Programming**: Tries all possible choices and stores results to reuse. It’s slower but always provides the optimal solution if the problem fits the DP pattern.
- **When to Choose Greedy**: If the problem has a simple structure and satisfies the greedy choice property and optimal substructure.

### 7. **Steps to Solve Greedy Problems**

1. **Understand the Problem**: Read the problem carefully and think about the constraints and requirements.
2. **Identify Optimal Substructure**: Check if the problem can be broken into subproblems that can be solved independently.
3. **Check for Greedy Choice Property**: Analyze if the locally optimal choice at each step will lead to a globally optimal solution.
4. **Sort/Organize Data**: Many greedy algorithms require data to be sorted in a specific way.
5. **Iteratively Apply Greedy Choices**: Solve the problem iteratively by making the best decision at each step.
6. **Edge Cases**: Consider edge cases, such as empty input, minimum/maximum values, etc.

### 8. **Common Greedy Problems on Leetcode**

#### 1. **Leetcode 435 - Non-overlapping Intervals**

- **Problem**: Find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
- **Strategy**: Sort intervals by end time, then greedily select the next non-overlapping interval.

```python
def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    end, count = float('-inf'), 0
    for start, finish in intervals:
        if start >= end:
            end = finish
        else:
            count += 1
    return count
```

#### 2. **Leetcode 134 - Gas Station**

- **Problem**: You need to complete a circuit around a series of gas stations, determining if you can start at one and complete the loop with available gas.
- **Strategy**: Greedily check if you can start from a given station and complete the circuit.

```python
def canCompleteCircuit(gas, cost):
    total_gas, total_cost, start, fuel = 0, 0, 0, 0
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        fuel += gas[i] - cost[i]
        if fuel < 0:
            start = i + 1
            fuel = 0
    return start if total_gas >= total_cost else -1
```

#### 3. **Leetcode 763 - Partition Labels**

- **Problem**: Partition a string into as many parts as possible so that no character appears in more than one part.
- **Strategy**: Track the last occurrence of each character and greedily partition the string.

```python
def partitionLabels(s):
    last = {c: i for i, c in enumerate(s)}
    j = anchor = 0
    result = []
    for i, c in enumerate(s):
        j = max(j, last[c])
        if i == j:
            result.append(i - anchor + 1)
            anchor = i + 1
    return result
```

#### 4. **Leetcode 406 - Queue Reconstruction by Height**

- **Problem**: Reconstruct a queue based on people's heights and their position.
- **Strategy**: Sort people by height in descending order and position them using a greedy approach.

```python
def reconstructQueue(people):
    people.sort(key=lambda x: (-x[0], x[1]))
    result = []
    for p in people:
        result.insert(p[1], p)
    return result
```

### 9. **Edge Cases to Consider in Greedy Problems**

- **Empty input**: Handle cases where there is no input.
- **Single element input**: Ensure the algorithm works for the minimum input size.
- **Maximum/minimum values**: Watch out for constraints related to the size of values (e.g., large numbers, edge boundaries).

### 10. **Practice Strategy**

- **Start small**: Begin with simpler greedy problems like activity selection or interval problems.
- **Work up**: Move to more complex problems involving graphs, partitioning, or combinations of constraints.
- **Check for correctness**: After writing your greedy solution, test it on both normal cases and edge cases.

### Conclusion

By mastering the principles behind greedy algorithms, recognizing problem patterns, and practicing with Leetcode problems, you can effectively solve a wide range of optimization problems.

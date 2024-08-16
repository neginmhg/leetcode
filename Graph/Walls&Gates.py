"""
You are given a 2D grid consisting of rooms, walls, and gates. The grid has three possible values:

-1 represents a wall or an obstacle.
0 represents a gate.
INF represents an empty room. It's a large integer value representing infinity, which means the room is empty and has not been assigned a distance to the nearest gate.
Your task is to fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, the room should remain INF.

"""

from collections import deque
from typing import List, Set, Tuple

class Solution:
    def walls_and_gates(self, rooms: List[List[int]]) -> None:
        """
        Fill each empty room with the distance to its nearest gate.
        If it is impossible to reach a gate, the room remains INF.
        """
        if not rooms or not rooms[0]:
            return
        
        # Constants
        ROWS, COLS = len(rooms), len(rooms[0])
        
        # Initialize the queue with all gates' positions
        queue = deque()
        visited = set()  # Set to track visited rooms
        
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))  # Mark gates as visited
        
        # Directions for moving in the grid: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Perform BFS from all gates
        while queue:
            r, c = queue.popleft()  # Get the current gate position
            for dr, dc in directions:
                nr, nc = r + dr, c + dc  # Calculate the neighbor's position
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    rooms[nr][nc] = rooms[r][c] + 1  # Update distance to nearest gate
                    queue.append((nr, nc))  # Add neighbor to the queue for further processing
                    visited.add((nr, nc))  # Mark the neighbor as visited

# Example usage
if __name__ == "__main__":
    rooms = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647]
    ]
    
    solution = Solution()
    solution.walls_and_gates(rooms)
    print(rooms)

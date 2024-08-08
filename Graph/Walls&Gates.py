"""
You are given a 2D grid consisting of rooms, walls, and gates. The grid has three possible values:

-1 represents a wall or an obstacle.
0 represents a gate.
INF represents an empty room. It's a large integer value representing infinity, which means the room is empty and has not been assigned a distance to the nearest gate.
Your task is to fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, the room should remain INF.

"""

from collections import deque

def walls_and_gates(rooms):
    if not rooms or not rooms[0]:
        return
    
    m, n = len(rooms), len(rooms[0])
    INF = 2**31 - 1
    queue = deque()

    # Add all gates to the queue
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                queue.append((i, j))
    
    # Directions for moving up, down, left, right
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # BFS from all gates
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == INF:
                rooms[nx][ny] = rooms[x][y] + 1
                queue.append((nx, ny))

# Example usage
rooms = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]

walls_and_gates(rooms)
print(rooms)

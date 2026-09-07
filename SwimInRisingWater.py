# Problem 778: Swim in Rising Water (Hard)
# Given an n x n grid of unique elevations, water rises over time t.
# At time t, you can swim to any adjacent cell whose elevation ≤ t.
# Goal: Find the minimum time t to reach (n-1, n-1) from (0, 0).
# Approach: Use Min-Heap BFS (Dijkstra-style) to always expand the lowest elevation reachable.
# Track the highest elevation encountered on the path — that’s the minimum time required.


import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = []
        visited = [[False] * n for _ in range(n)]
        current_elev = grid[0][0]
        heapq.heappush(queue, (current_elev, 0, 0))
        visited[0][0] = True
        t = 0
        while queue:
            current_elev, r, c = heapq.heappop(queue)
            t = max(t, current_elev)
            if r == n - 1 and c == n - 1:
                return t
            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    next_elev = grid[nr][nc]
                    heapq.heappush(queue, [next_elev, nr, nc])
                    visited[nr][nc] = True





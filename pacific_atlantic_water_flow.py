# Given an m x n grid of elevations, determine which cells can flow water to both the Pacific and Atlantic oceans.
# Pacific touches the top and left edges; Atlantic touches the bottom and right edges.
# Water flows from a cell to neighboring cells (up, down, left, right) if the neighbor's height is ≤ current cell.
# Return all coordinates [r, c] where water can reach both oceans.

class Solution:
    def pacificAtlantic(self, heights):
        m = len(heights)
        n = len(heights[0])
        pacific = []
        atlantic = []
        result = []

        pacvisited = [[False] * n for _ in range(m)]
        atvisited = [[False] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    pacific.append([r, c])
                    pacvisited[r][c] = True
                if r == m - 1 or c == n - 1:
                    atlantic.append([r, c])
                    atvisited[r][c] = True

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while pacific:
            r, c = pacific.pop()
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < m and 0 <= nc < n and heights[r][c] <= heights[nr][nc] and not pacvisited[nr][nc]:
                    pacvisited[nr][nc] = True
                    pacific.append((nr, nc))

        while atlantic:
            r, c = atlantic.pop()
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < m and 0 <= nc < n and heights[r][c] <= heights[nr][nc] and not atvisited[nr][nc]:
                    atvisited[nr][nc] = True
                    atlantic.append((nr, nc))
        for r in range(m):
            for c in range(n):
                if pacvisited[r][c] and atvisited[r][c]:
                    result.append([r, c])
        return result








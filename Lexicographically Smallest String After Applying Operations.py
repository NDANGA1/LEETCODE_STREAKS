# ==========================================================
# Problem: 1625. Lexicographically Smallest String After Applying Operations
# ----------------------------------------------------------
# You are given:
#   - A string `s` of even length, containing digits [0–9]
#   - Two integers `a` and `b`
#
# You can repeatedly apply two operations, in any order, any number of times:
#   1. Add operation: Add `a` (mod 10) to every digit at odd indices (0-indexed)
#   2. Rotate operation: Rotate the entire string to the right by `b` positions
#
# Goal:
#   Find the lexicographically smallest string that can be obtained through any
#   sequence of these operations.
#
# Example:
#   s = "5525", a = 9, b = 2
#   -> The smallest reachable string is "2050".
#
# ----------------------------------------------------------
# Intuition of the Problem:
# - These operations define a finite set of reachable strings because:
#       • Adding a modulo 10 cycles digits
#       • Rotating by b repeatedly cycles the string
# - Therefore, we can treat this as a graph problem:
#       Each unique string is a node
#       Each operation creates edges between strings
# - We must explore all reachable strings and pick the smallest one lexicographically.
#
# ----------------------------------------------------------
# Solution Intuition (Breadth-First Search):
# - Use BFS to explore all possible string states.
# - From any string, we can create two new ones:
#       → One by applying the add operation
#       → One by applying the rotate operation
# - Keep track of visited strings to avoid re-processing and infinite loops.
# - Keep updating the smallest lexicographic string found so far.
#
# ----------------------------------------------------------
# Key Logical Points:
# - Modular addition ensures digits wrap around correctly after 9.
# - Rotations can bring any character to the front over time.
# - The number of possible states is finite due to periodic repetition.
# - BFS ensures all reachable transformations are explored once.
# - Lexicographic comparison can be done directly using Python’s min().
#
# ----------------------------------------------------------
# Time Intuition:
# - Although operations can repeat infinitely, the reachable state space is small,
#   because there are at most 10 * len(s) unique "add" states and len(s) unique rotations.
#
# ----------------------------------------------------------
# This BFS guarantees the correct smallest string because it explores
# every reachable state and always records the minimum seen.
# ==========================================================

from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q = deque([s])        # BFS queue starts with the initial string
        smallest = s          # Store the smallest string found so far
        visited = set()       # Track all processed states

        while q:
            curr = q.popleft()  # Take the next string from the queue

            if curr in visited:
                continue        # Skip if this state has already been processed
            visited.add(curr)   # Mark this state as visited

            # Update smallest if current string is lexicographically smaller
            smallest = min(smallest, curr)

            # Operation 1: Add 'a' to digits at odd indices (mod 10)
            arr = list(curr)
            for i in range(1, len(arr), 2):           # Only odd indices
                arr[i] = str((int(arr[i]) + a) % 10)  # Add with wrap-around
            added = ''.join(arr)                      # Convert back to string

            # Operation 2: Rotate the string right by 'b' positions
            rotated = curr[-b:] + curr[:-b]

            # Add both new states to the queue if not yet visited
            if added not in visited:
                q.append(added)
            if rotated not in visited:
                q.append(rotated)

        # Return the smallest string found after exploring all reachable states
        return smallest

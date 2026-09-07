# 3461. Check If Digits Are Equal in String After Operations I
# --------------------------------------------------------------------
# Problem Intuition:
# You are given a string `s` containing digits.
# In each operation:
#   - Take every pair of consecutive digits in `s`.
#   - Replace that pair with a single digit = (sum of the two digits) % 10.
#   - Continue performing this operation until only two digits remain.
#
# The task: Check if the final two digits are equal.
#
# --------------------------------------------------------------------
# Example:
# s = "3902"
# Step 1: (3+9)%10=2, (9+0)%10=9, (0+2)%10=2 → s = "292"
# Step 2: (2+9)%10=1, (9+2)%10=1 → s = "11"
# Final result = True (both digits are the same)
#
# --------------------------------------------------------------------
# Problem Intuition:
# The process is a chain reduction.
# Each iteration compresses s by replacing consecutive pairs
# with their mod-10 sums.
# The digits interact locally (each new digit only depends on two neighbors).
#
# Since the length shrinks by 1 per round, we stop when len(s) == 2,
# and check if the two digits are identical.
#
# --------------------------------------------------------------------
# Solution Intuition (Two Approaches):
#
# 1. Simulation Approach (Detailed, Stepwise)
#    - Pop the first element, pair with the next, append result to the end.
#    - Restart after consuming all pairs in one round.
#    - Works by continuously mutating the list in-place.
#
# 2. Optimized Clean Approach
#    - Build a new list of sums in each round.
#    - Replace `s` with that new list until only two remain.
#    - Simpler, more readable, and more efficient (no pop(0)).
#
# --------------------------------------------------------------------
# Time Complexity:
# - Solution 1: O(n³) (pop(0) shifts all elements each time)
# - Solution 2: O(n²)
#
# Space Complexity:
# - Both use O(n) auxiliary space for storing digits.


# --------------------------------------------------------------------
# SOLUTION 1: Simulation-Based Approach (User's Original)
# --------------------------------------------------------------------
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Convert string to list of integers
        s = [int(char) for char in s]
        n = len(s)
        i = 1  # pointer to track pair count within one round

        # Keep reducing until only two digits remain
        while len(s) > 2:
            x = s.pop(0)  # take the first digit

            if i == n - 1:  # reached end of current round
                y = s.pop(0)  # take last available digit
                s.append((x + y) % 10)  # append their mod-10 sum
                n = len(s)  # reset new length
                i = 1       # restart next round
                print(s)    # debug trace (optional)
            else:
                y = s[0]  # look at next digit (not removing it)
                s.append((x + y) % 10)
                i += 1  # move to next pair

        # After loop, check final two digits
        print(s)  # debug trace (optional)
        return len(s) == 2 and s[0] == s[1]


# --------------------------------------------------------------------
# SOLUTION 2: Simplified and Optimized Approach
# --------------------------------------------------------------------
class Solution2:
    def hasSameDigits(self, s: str) -> bool:
        # Convert to list of digits
        s = [int(c) for c in s]

        # Keep reducing until only two digits remain
        while len(s) > 2:
            new_s = []
            # Build next sequence by summing consecutive pairs mod 10
            for i in range(len(s) - 1):
                new_s.append((s[i] + s[i + 1]) % 10)
            s = new_s  # move to next iteration

        # Return whether last two digits are equal
        return s[0] == s[1]


# --------------------------------------------------------------------
# Example Run
# s = "3902"
# sol1 = Solution()
# print(sol1.hasSameDigits(s))   # True
# sol2 = Solution2()
# print(sol2.hasSameDigits(s))   # True
# --------------------------------------------------------------------

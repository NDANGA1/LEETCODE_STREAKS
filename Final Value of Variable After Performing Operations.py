# Problem: 2011. Final Value of Variable After Performing Operations
# ----------------------------------------------------------
# We are given:
#   - A variable X, initially equal to 0
#   - A list of string operations, each being one of:
#         "++X", "X++"  → increment X by 1
#         "--X", "X--"  → decrement X by 1
#
# Task:
#   After performing all operations in the given order,
#   return the final value of X.
#
# ----------------------------------------------------------
# Example:
#   Input:  operations = ["--X","X++","X++"]
#   Steps:
#       X = 0
#       "--X" → X = -1
#       "X++" → X =  0
#       "X++" → X =  1
#   Output: 1
#
# ----------------------------------------------------------
# Intuition:
# - Every operation either increases or decreases X by 1.
# - The prefix (++X) or postfix (X++) form does not matter;
#   both increment by the same amount.
# - Similarly, (--X) or (X--) both decrement by the same amount.
# - Therefore, we only need to count how many increments (+1)
#   and decrements (-1) occur.
#
# ----------------------------------------------------------
# Solution Intuition:
# - Initialize X = 0
# - For each operation:
#       • If it contains '+', increment X
#       • Otherwise, decrement X
# - Return the final X value.
#
# This approach is O(n) in time and O(1) in space.
# ----------------------------------------------------------

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0  # start value

        for op in operations:
            # Both "X++" and "++X" mean increment
            if op == "X++" or op == "++X":
                x += 1
            else:
                # Both "X--" and "--X" mean decrement
                x -= 1

        # Return final value after all operations
        return x

# -------------------------------------------------------------------------
# Problem: 2598. Smallest Missing Non-negative Integer After Operations
# -------------------------------------------------------------------------
# You are given an integer array `nums` and an integer `value`.
# In one operation, you can add or subtract `value` from any element of `nums`.
#
# The task is to determine the **maximum possible MEX (Minimum Excluded Number)**
# that can be achieved after applying any number of such operations.
#
# MEX of an array = the smallest non-negative integer NOT present in the array.
#
# Example:
# nums = [1, -10, 7, 13, 6, 8], value = 5
# -> Maximum MEX = 4
#
# -------------------------------------------------------------------------
# Intuition Summary:
# -------------------------------------------------------------------------
# Each number can be adjusted by multiples of `value`, meaning its *remainder*
# when divided by `value` (num % value) determines the class of numbers it can
# represent after any number of additions/subtractions.
#
# For instance, with value = 5:
#   -10 % 5 == 0  ➜ can generate { ..., -10, -5, 0, 5, 10, 15, ... }
#
# So, for each remainder class, we can only use as many numbers as exist in that
# remainder bucket before we "run out" of representable numbers.
#
# The idea:
# - Count how many numbers fall into each remainder group (mod value).
# - Start from x = 0 and check if we can represent it using available remainders.
#   → If remainder (x % value) exists in freq, decrement its count and move to next x.
#   → If remainder not available, x is the smallest missing number (MEX).
#
# This greedy simulation continues until we can no longer construct the next integer.
#
# Time Complexity: O(n)
# Space Complexity: O(value)
# -------------------------------------------------------------------------

from collections import Counter


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # Step 1: Normalize numbers by their modulo class
        mods = [num % value for num in nums]

        # Step 2: Count how many numbers fall into each remainder bucket
        freq = Counter(mods)

        # Step 3: Try constructing consecutive integers starting from 0
        x = 0
        while True:
            rem = x % value  # remainder of current number x

            # If we have available numbers in this remainder bucket,
            # use one to represent x and move to the next integer
            if freq[rem] > 0:
                freq[rem] -= 1
                x += 1
            else:
                # As soon as we cannot form x, it becomes our MEX
                return x

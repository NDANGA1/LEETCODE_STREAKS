# Problem Intuition:
# ---------------------
# You are given an integer array `nums` and an integer `k`.
# For each number x in nums, you can add any integer in the range [-k, k] *at most once*.
# Your goal is to maximize the number of distinct elements in the final array.
#
# Example:
#   nums = [4,4,4,4], k = 1
#   We can modify them to [3,4,5] → 3 distinct numbers.
#
# Key insight:
#   - Each number x can become anything within [x - k, x + k].
#   - We want as many unique integers as possible overall.
#   - So, we greedily choose the smallest possible available number
#     for each element, staying within its valid range.
#
# Why greedy works:
#   - Sorting ensures we deal with smaller numbers first.
#   - For each element, picking the *smallest valid unused value*
#     leaves room for future (larger) elements to find distinct values.
#
# Complexity:
#   - Sorting: O(n log n)
#   - Single scan (greedy): O(n)
#   - Total: O(n log n), efficient for n ≤ 10⁵

from typing import List
from math import inf

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # Step 1️⃣: Sort numbers to handle them in ascending order
        nums.sort()

        # `curr` marks the smallest number we can still use next
        # Initialize to -infinity so first pick is always allowed
        curr = -inf
        distinct = 0  # counts how many distinct numbers we have chosen

        # Step 2️⃣: For each number, try to assign a unique possible value
        for x in nums:
            # Each number x can vary between [x - k, x + k]
            # We want the smallest number >= curr within this range
            pick = max(x - k, curr)

            # If that pick is still ≤ x + k, it is valid
            if pick <= x + k:
                # We successfully assign a distinct number
                distinct += 1
                # Move `curr` to next unused number
                curr = pick + 1

        # Step 3️⃣: Return total distinct numbers achievable
        return distinct


# Example walkthrough:
# nums = [4,4,4,4], k = 1
# Sorted = [4,4,4,4]
# Iteration:
#   x=4 → pick=max(3,-inf)=3 ≤5 → distinct=1, curr=4
#   x=4 → pick=max(3,4)=4 ≤5 → distinct=2, curr=5
#   x=4 → pick=max(3,5)=5 ≤5 → distinct=3, curr=6
#   x=4 → pick=max(3,6)=6>5 stop
# Output = 3 distinct numbers

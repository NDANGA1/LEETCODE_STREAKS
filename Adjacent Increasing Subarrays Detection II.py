"""
Problem Summary:
----------------
Given an array nums of n integers, find the maximum value of k such that there exist two
adjacent subarrays of length k, each strictly increasing. The second subarray must start
immediately after the first one. A subarray is a contiguous sequence of elements.

Examples:
- nums = [2,5,7,8,9,2,3,4,3,1] → Output: 3
  Explanation: Adjacent increasing subarrays of length 3 are [7,8,9] and [2,3,4].

- nums = [1,2,3,4,4,4,4,5,6,7] → Output: 2
  Explanation: Adjacent increasing subarrays of length 2 are [1,2] and [3,4].

Intuition & Approach:
---------------------
1. For each index, compute:
   - L[i]: length of strictly increasing subarray ending at index i.
   - R[i]: length of strictly increasing subarray starting at index i.

2. For any possible split between index i and i+1, the maximum k is:
      min(L[i], R[i+1])
   because the first subarray can be at most L[i] and the second at most R[i+1].

3. The global answer is the maximum value of min(L[i], R[i+1]) across all splits.

This approach efficiently finds the largest k in O(n) time using two passes to compute L and R,
and one pass to find the maximum min(L[i], R[i+1]).

Solution:
---------
"""


class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        L = [1] * n  # length of increasing subarray ending at i
        R = [1] * n  # length of increasing subarray starting at i

        # Fill L: lengths of increasing subarrays ending at i
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                L[i] = L[i - 1] + 1

        # Fill R: lengths of increasing subarrays starting at i
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                R[i] = R[i + 1] + 1

        # Compute maximum k from adjacent subarrays
        ans = 0
        for i in range(n - 1):
            ans = max(ans, min(L[i], R[i + 1]))

        return ans

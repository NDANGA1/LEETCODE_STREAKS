# ------------------------------------------------------------------------------------
# 3186. Maximum Total Damage With Spell Casting
# ------------------------------------------------------------------------------------
# 🧙 Problem Summary:
# A magician can cast multiple spells, each having a damage value given in the array `power`.
# However, if the magician casts a spell with damage `x`, they cannot cast any spell
# with damage `x ± 1` or `x ± 2`.
# Each spell can only be cast once. We must return the maximum possible total damage.
#
# ------------------------------------------------------------------------------------
# 💡 Example 1:
# Input:  power = [1, 1, 3, 4]
# Output: 6
# Explanation: Cast spells with damage 1, 1, and 4 → total = 6
#
# 💡 Example 2:
# Input:  power = [7, 1, 6, 6]
# Output: 13
# Explanation: Cast spells with damage 1, 6, 6 → total = 13
#
# ------------------------------------------------------------------------------------
# 🧠 Approach:
# 1. Count how many spells have each distinct damage value using Counter().
# 2. Sort unique damage values in ascending order.
# 3. Use dynamic programming where:
#    - dp[i] = max total damage achievable considering values up to vals[i].
#    - For each vals[i], either:
#         (a) skip this damage value → dp[i-1]
#         (b) take it → (vals[i] * count) + dp[j],
#             where j is the last index with vals[j] ≤ vals[i] - 3 (non-conflicting).
#    - Find j efficiently with binary search.
# 4. Return dp[-1] as the maximum possible total damage.
#
# ------------------------------------------------------------------------------------
# ⏱️ Time Complexity:  O(n log n)
#    - Counting: O(n)
#    - Sorting unique damages: O(u log u)
#    - DP with binary search: O(u log u)
#      where u = number of unique damage values
#
# 🧮 Space Complexity: O(u)
#
# ------------------------------------------------------------------------------------
# ✅ Efficient and accepted solution (no Time Limit Exceeded)
# ------------------------------------------------------------------------------------

from collections import Counter
from bisect import bisect_left
from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        c = Counter(power)
        vals = sorted(c)
        n = len(vals)

        dp = [0] * n
        dp[0] = vals[0] * c[vals[0]]

        for i in range(1, n):
            # Option 1: skip current damage value
            skip = dp[i-1]

            # Option 2: take current damage value
            take = vals[i] * c[vals[i]]
            j = bisect_left(vals, vals[i] - 2) - 1  # find last non-conflicting index
            if j >= 0:
                take += dp[j]

            dp[i] = max(skip, take)

        return dp[-1]

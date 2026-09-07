# Problem: 3346. Maximum Frequency of an Element After Performing Operations I
#
# You're given:
#   - An integer array `nums`
#   - Two integers `k` and `numOperations`
#
# You can perform exactly `numOperations` operations.
# In each operation:
#   - Pick an unused index i
#   - Add any integer from [-k, k] to nums[i]
#
# Goal:
#   After all operations, find the maximum possible frequency
#   (number of identical elements) achievable in the array.
#
# Intuition:
# ------------------------------------------------------------
# 1. Each number nums[i] can move within a range:
#       [nums[i] - k, nums[i] + k]
#
# 2. Two numbers can become equal if their movement ranges overlap.
#    So we are looking for the largest group of numbers whose
#    [min_range, max_range] intervals overlap.
#
# 3. Sorting helps because overlapping ranges appear next to each other.
#
# 4. Use a sliding window [l, r]:
#    - Expand the right pointer while the current range (max - min) ≤ 2*k.
#    - If the range exceeds 2*k, move the left pointer to shrink the window.
#
# 5. Within a valid window:
#    - Some numbers may already be equal (their frequency is max_dup).
#    - We can modify at most `numOperations` other elements to match them.
#
# 6. Therefore, for each window:
#       window_size = r - l + 1
#       possible_frequency = min(window_size, max_dup + numOperations)
#
# 7. Keep track of the maximum possible frequency across all windows.
#


from collections import Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # Step 1: Sort to allow sliding window comparison
        nums.sort()
        n = len(nums)

        l = 0                        # Left pointer of sliding window
        count = Counter()             # Track frequencies within window
        max_freq = 1                  # At least one number itself

        # Step 2: Expand sliding window
        for r in range(n):
            count[nums[r]] += 1       # Include rightmost element

            # Step 3: Ensure window remains within valid range
            while nums[r] - nums[l] > 2 * k:
                # If window exceeds movement range, remove from left
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1

            # Step 4: Measure current window
            window_size = r - l + 1
            max_dup = max(count.values())     # Most frequent number in window

            # Step 5: Compute possible max frequency in this window
            possible_freq = min(window_size, max_dup + numOperations)

            # Step 6: Track the best frequency found
            max_freq = max(max_freq, possible_freq)

        return max_freq

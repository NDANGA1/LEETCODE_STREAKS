# 3349. Adjacent Increasing Subarrays Detection I
#
# Given an array nums of n integers and an integer k, determine whether there exist
# two adjacent subarrays of length k such that both subarrays are strictly increasing.
# Specifically, check if there are two subarrays starting at indices a and b (a < b), where:
#
#   • Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
#   • The subarrays must be adjacent, meaning b = a + k.
#
# Return True if it is possible to find two such subarrays, and False otherwise.
#
# Example 1:
# Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3
# Output: True
# Explanation:
#   The subarray starting at index 2 is [7,8,9], which is strictly increasing.
#   The subarray starting at index 5 is [2,3,4], which is also strictly increasing.
#   These two subarrays are adjacent, so the result is True.
#
# Example 2:
# Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5
# Output: False
#
# Constraints:
#   2 <= nums.length <= 100
#   1 < 2 * k <= nums.length
#   -1000 <= nums[i] <= 1000


# ------------------ Solution ------------------

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        

        s1 = 0           # Start index of the first subarray
        s2 = k           # Start index of the second subarray (must be adjacent)
        n = len(nums)
        no_trues = 0     # Counter to track consecutive 'increasing' pairs

        # Base case:
        # Any single-element subarray (k == 1) is vacuously strictly increasing.
        # Hence, two adjacent elements automatically satisfy the condition.
        if k == 1:
            return True

        # Loop while ensuring both (s1+1) and (s2+1) are within array bounds.
        while s2 <= n - 2:
            # Check if both current windows have an increasing step at the same offset.
            if nums[s1 + 1] > nums[s1] and nums[s2 + 1] > nums[s2]:
                no_trues += 1
                # If we've seen (k - 1) consecutive increasing pairs in both windows,
                # it means both subarrays of length k are strictly increasing.
                if no_trues == k - 1:
                    return True
            else:
                # Reset counter if either subarray stops increasing.
                no_trues = 0

            # Slide both windows forward by one position.
            s1 += 1
            s2 += 1

        # If loop completes without finding adjacent increasing subarrays, return False.
        return False

# 3354. Make Array Elements Equal to Zero
# Problem Summary:
# You are given an integer array nums. You start from any position curr such that nums[curr] == 0
# and choose an initial direction — either left or right.
# Then you repeatedly perform these steps:
#   1. If curr is out of range, stop.
#   2. If nums[curr] == 0, move one step in the current direction.
#   3. If nums[curr] > 0, decrease it by 1, reverse the direction, and move one step in the new direction.
# A starting position and direction are considered valid if, by the end of the process,
# every element in nums becomes 0.
#
# The task is to return how many valid (starting position, direction) combinations exist.
#
# Example:
#   Input: nums = [1,0,2,0,3]
#   Output: 2
#   Explanation: Starting from index 3 going left or right both result in all zeros.
#
# Constraints:
#   1 <= nums.length <= 100
#   0 <= nums[i] <= 100
#   There is at least one index i such that nums[i] == 0
#--------------------------------------------------------------------------------------------------
# The key observation:
# Every move either reduces some element by 1 or skips over zeros.
# For the process to finish with all zeros, the total “weight” (sum of nums) on both sides of a zero
# must be balanced so that decrements distribute evenly in both directions.

# Solution Intuition:
# For every index where nums[i] == 0, we check the difference between:
#   - the total sum of elements to the left (sum(nums[:i]))
#   - and the total sum of elements to the right (sum(nums[i+1:]))
# If these two sums are equal, then starting from that zero, moving either direction is valid → +2 ways.
# If the difference between them is 1, then only one direction (toward the heavier side) can balance it → +1 way.
# Otherwise, it’s impossible from that zero.
#
# This balance-based reasoning avoids simulation, making the solution efficient and elegant.
#----------------------------------------------------------------------------------------------------
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        zeros = [i for i, x in enumerate(nums) if x == 0]  # indices of all zeros
        valid = 0  # number of valid starting options

        for i in zeros:
            # Calculate sums on left and right sides of this zero
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i + 1:])
            diff = abs(left_sum - right_sum)

            # If sums are equal, both left and right directions work
            if diff == 0:
                valid += 2
            # If sums differ by 1, only one direction works
            elif diff == 1:
                valid += 1

        return valid

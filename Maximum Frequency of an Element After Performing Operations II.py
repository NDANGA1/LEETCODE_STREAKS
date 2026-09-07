# 3347. Maximum Frequency of an Element After Performing Operations II
# --------------------------------------------------------------------
# Problem Intuition:
# Each number nums[i] can be moved anywhere in the range [nums[i] - k, nums[i] + k].
# Two or more numbers can become equal if their ranges overlap at some integer point T.
#
# Our goal:
#     Perform at most `numOperations` moves (changing distinct indices),
#     to maximize how many elements become equal to some integer value T.
#
# Observation:
# - If T lies inside many ranges [x - k, x + k], those x-values can all be shifted to T.
# - If T equals one of the original nums[i], that number doesn’t require a move.
#
# So, for each possible T, the number of elements that *can* become T is:
#     s(T) = number of ranges covering T
# And the number of elements that *are already* T is:
#     cnt[T]
#
# Therefore, the total we can make equal to T is:
#     min(s(T), cnt[T] + numOperations)
#
# We seek the maximum value of this expression across all T.
#
# --------------------------------------------------------------------
# Solution Intuition:
# - Use a *line sweep* (difference array) approach to efficiently compute s(T):
#   For each interval [x - k, x + k], add +1 at (x - k) and -1 at (x + k + 1).
# - Traverse all sorted coordinates (where changes occur).
# - Maintain a running sum `s`, representing how many intervals currently overlap.
# - For each coordinate:
#     1. If it’s an original number value, consider `min(s, cnt[pos] + numOperations)`.
#     2. For in-between integer points (segments between events), consider `min(s, numOperations)`,
#        since those T are not originally in nums.
# - Track and return the global maximum.
#
# Time Complexity: O(n log n) due to sorting coordinates.
# Space Complexity: O(n) for event maps and counters.


from typing import List
from collections import defaultdict, Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # Edge cases
        if not nums:
            return 0

        n = len(nums)
        cnt = Counter(nums)  # counts of exact original values

        # Build events for inclusive intervals [x-k, x+k]:
        # +1 at L, -1 at R+1 so that coverage s(T) for integer T is correct.
        events = defaultdict(int)
        for x in nums:
            L = x - k
            R = x + k
            events[L] += 1
            events[R + 1] -= 1

        # Interesting coordinates to sweep:
        # include all event keys (where coverage changes) and all unique original values
        coords = sorted(set(events.keys()) | set(cnt.keys()))

        s = 0          # current coverage (how many intervals cover current position)
        ans = 0

        # Sweep through coordinates in ascending order.
        # For each coordinate 'pos' we:
        #  1) apply events[pos] to update coverage s at pos
        #  2) consider the point pos itself if it's an original value (cnt[pos] > 0)
        #  3) consider the open segment [pos, next_pos - 1] (if any) where coverage is constant s,
        #     and for T not equal to an original value in that segment we have cnt[T] = 0,
        #     so candidate = min(s, numOperations).
        for i, pos in enumerate(coords):
            # Apply all events at pos to update coverage (s is coverage *at pos*)
            s += events[pos]

            # If pos is an original value, consider target = pos with cnt[pos] originals.
            if pos in cnt:
                # total elements that can be converted to 'pos' = s (all intervals covering pos)
                # we can add up to numOperations extra converted elements to the existing cnt[pos],
                # so achievable = min(s, cnt[pos] + numOperations)
                candidate = min(s, cnt[pos] + numOperations)
                if candidate > ans:
                    ans = candidate
                # early exit
                if ans == n:
                    return n

            # Consider the segment of integer points strictly after pos and before next_pos (if any)
            # On this segment coverage stays equal to s (because events only at coords).
            # These integer T are not equal to any original value unless there's an original
            # exactly inside (we included original values in coords so segment excludes them).
            if i + 1 < len(coords):
                next_pos = coords[i + 1]
                # There exist integer points T with pos <= T <= next_pos - 1.
                # We must ensure the segment contains at least one integer:
                if pos <= next_pos - 1:
                    # For such T with cnt == 0, achievable = min(s, numOperations)
                    candidate = min(s, numOperations)
                    if candidate > ans:
                        ans = candidate
                    if ans == n:
                        return n
            else:
                # Last coordinate: there may be no segment beyond; nothing further to check.
                pass

        return ans

# Problem Intuition:
# ------------------
# We are given a string `s` and an integer `k`.
# We can change **at most one character** in `s` to any other lowercase letter.
# Then, we repeatedly partition `s` greedily: take the longest prefix with at most `k` distinct characters.
# We want to maximize the number of partitions after doing the optimal single change.

# Key insight:
# - The number of partitions depends on the distribution of distinct letters.
# - Changing a character to a **new letter** can split an existing block of length > 1 into multiple partitions.
# - For correctness, we must simulate the partitions **after each possible change**, because a single change may propagate splits downstream.

# Solution Intuition:
# ------------------
# 1. Compute the partitions of the original string without any change.
# 2. For each index `i`, try changing `s[i]` to any other letter (`'a'` to `'z'`) except itself.
# 3. For each modified string, greedily count partitions using a sliding window.
# 4. Keep track of the maximum partitions among all possibilities.
# Note: This approach is O(n*26), which is acceptable for moderate n (~10^4).

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)

        # Helper function: greedily count partitions
        def count_partitions(arr):
            partitions = 0
            seen = set()  # track distinct characters in current partition
            for ch in arr:
                seen.add(ch)
                if len(seen) > k:  # current partition exceeded k distinct letters
                    partitions += 1      # finish current partition
                    seen = {ch}          # start new partition with current char
            return partitions + 1      # add the last partition

        # Step 1: compute base partitions without any change
        ans = count_partitions(s)

        # Step 2: simulate changing each character to every other letter
        for i in range(n):
            original = s[i]
            for c in map(chr, range(97, 123)):  # 'a' to 'z'
                if c == original:
                    continue  # skip original character, we want a "change"
                t = s[:i] + c + s[i+1:]  # create new string with the change
                # Step 3: compute partitions for the modified string
                ans = max(ans, count_partitions(t))  # keep maximum partitions

        return ans

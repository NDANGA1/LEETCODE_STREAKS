# Problem:
# Unlock computer i only if there exists j < i with complexity[j] < complexity[i].
# 0 is already unlocked and must appear first in the order.
# Count how many valid permutations exist.

# Key logic:
# A valid order exists ONLY if complexity[0] is strictly the smallest.
# If true → any order after 0 works → (n-1)! permutations.
# If false → some computer can never be unlocked → return 0.


class Solution:
    def countPermutations(self, complexity):
        MOD = 10**9 + 7
        n = len(complexity)

        # Check if complexity[0] is strictly smallest
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0

        # Compute (n-1)! modulo MOD
        perm = 1
        for x in range(2, n):
            perm = (perm * x) % MOD

        return perm


# Quick tests
if __name__ == "__main__":
    s = Solution()
    print(s.countPermutations([1,2,3]))         # 2
    print(s.countPermutations([3,3,3,4,4]))     # 0
    print(s.countPermutations([3,5,2]))         # 0
    print(s.countPermutations([1,4,2,5]))       # 6

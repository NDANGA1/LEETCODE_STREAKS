# 3539. Find Sum of Array Product of Magical Sequences
# -------------------------------------------------------------------------
# Fully annotated Python implementation with detailed explanations.
#
# Goal recap (short):
# - We form ordered sequences `seq` of length m whose entries are indices 0..n-1.
# - A sequence is "magical" if popcount(sum(2**seq[i])) == k.
# - For each magical sequence we add product(nums[seq[0]] * ... * nums[seq[m-1]]).
# - Return the sum modulo MOD.
#
# Key high-level idea:
# - Work with counts c[i] = how many times index i is used (multiset view).
# - Use DP to iterate indices and simulate binary addition using a carry.
# - Track number of picks used (t), current carry, and number of 1-bits so far.
# - Factor ordering by m! and account for repeated picks by dividing by c[i]! in DP
#   (we incorporate inverse factorials).
# -------------------------------------------------------------------------

from typing import List

class Solution:
    def findSum(self, m: int, k: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # -------------------------
        # 1) Factorials and inverse factorials (modular) — why?
        # -------------------------
        # We will count ordered sequences, but we enumerate by counts c[i] (unordered).
        # The number of ordered sequences corresponding to counts c is:
        #     m! / (c[0]! * c[1]! * ... * c[n-1]!)
        # We factor out m! and compute DP contributions for:
        #     Π ( nums[i]^c[i] / c[i]! )
        # At the end multiply DP result by m!.
        #
        # So we need factorials and modular inverses for c! terms.
        #
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i % MOD

        # Compute invfact using Fermat's little theorem:
        # invfact[m] = fact[m]^(MOD-2) mod MOD, then downward fill
        invfact = [1] * (m + 1)
        invfact[m] = pow(fact[m], MOD - 2, MOD)
        for i in range(m - 1, -1, -1):
            invfact[i] = invfact[i + 1] * (i + 1) % MOD

        # -------------------------
        # 2) Precompute powers nums[i]^c for c in 0..m — why?
        # -------------------------
        # In the DP transition we will repeatedly multiply by nums[i]^c for many c.
        # Precomputing makes each lookup O(1) and avoids repeated pow calls.
        pow_table = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            # pow_table[i][0] = 1 already set
            for c in range(1, m + 1):
                pow_table[i][c] = (pow_table[i][c - 1] * nums[i]) % MOD

        # -------------------------
        # 3) DP structure
        # -------------------------
        # We'll maintain dp[t][carry][bits] = cumulative sum of:
        #   Π ( nums[j]^c[j] / c[j]! )
        # over assignments for processed indices, where:
        #   - t is total number of picks used so far (sum c[j] for processed indices)
        #   - carry is the carry that will be added to the next bit position
        #   - bits is number of 1-bits counted among processed bit positions
        #
        # Ranges:
        #   t in 0..m
        #   carry in 0..m   (carry can't exceed m because we add at most m copies)
        #   bits in 0..k    (we can prune if bits > k)
        #
        # We use a rolling/2-layer DP: process one index at a time and build next_dp.
        #
        # Note: we use (k+2) and (m+2) sized arrays to avoid index errors when incrementing.
        dp = [[[0] * (k + 2) for _ in range(m + 2)] for _ in range(m + 2)]
        dp[0][0][0] = 1  # base: no picks, no carry, zero bits, contribution 1 (empty product)

        # -------------------------
        # 4) Iterate indices (simulate adding c[i]*2^i)
        # -------------------------
        # For each index i we decide how many times (c) we pick it (0..m-t).
        # Binary addition logic for a single bit position i:
        #   total = carry + c
        #   bit_at_i = total % 2
        #   next_carry = total // 2
        #
        # We incorporate multiplication by nums[i]^c and division by c! (via invfact[c]).
        # Also prune if bits exceed k (no need to continue).
        for i in range(n):
            # next_dp re-initialized for the next index
            next_dp = [[[0] * (k + 2) for _ in range(m + 2)] for _ in range(m + 2)]

            # iterate over all possible partial states
            for t in range(m + 1):            # how many picks used so far
                for carry in range(m + 1):    # current carry into this bit
                    for bits in range(k + 1): # number of 1 bits seen so far (limited by k)
                        cur_val = dp[t][carry][bits]
                        if cur_val == 0:
                            continue  # no contribution from this state

                        # choose c times index i (0..remaining picks)
                        # remaining picks allowed = m - t
                        # we loop c from 0 up to that number (inclusive)
                        max_c = m - t
                        for c in range(max_c + 1):
                            total = carry + c
                            bit_here = total & 1               # same as total % 2
                            new_carry = total >> 1            # same as total // 2
                            new_bits = bits + bit_here

                            # prune: if we've already exceeded k bits we don't need to track
                            if new_bits > k:
                                continue

                            # DP multiplicative factor:
                            # multiply current partial value by nums[i]^c / c!
                            # - pow_table[i][c] gives nums[i]^c % MOD
                            # - invfact[c] gives 1/c! % MOD
                            add_val = (cur_val * pow_table[i][c]) % MOD
                            add_val = (add_val * invfact[c]) % MOD

                            # accumulate into next state
                            next_dp[t + c][new_carry][new_bits] = (
                                next_dp[t + c][new_carry][new_bits] + add_val
                            ) % MOD

            # move to next index
            dp = next_dp

        # -------------------------
        # 5) Final aggregation
        # -------------------------
        # After processing all indices, relevant states are dp[m][carry][bits]
        # (we must have used exactly m picks).
        # But bits counts only 1s in positions 0..n-1. We must also include 1s
        # from the remaining `carry` bits (carry can extend beyond n-1 positions).
        #
        # A final state is valid if bits + popcount(carry) == k.
        # For each valid state we add its dp value; finally multiply by m! to
        # convert from unordered count-product to ordered sequence products.
        result = 0
        for carry in range(m + 1):
            for bits in range(k + 1):
                val = dp[m][carry][bits]
                if val == 0:
                    continue
                # add popcount of carry (carry <= m so small)
                total_bits = bits + bin(carry).count("1")
                if total_bits == k:
                    result = (result + val) % MOD

        # multiply by m! to account for permutations (ordered sequences)
        result = result * fact[m] % MOD
        return result


# -------------------------
# Quick usage examples (matches problem samples)
# -------------------------
if __name__ == "__main__":
    s = Solution()
    # Example 1
    print(s.findSum(5, 5, [1, 10, 100, 10000, 1000000]))  # -> 991600007
    # Example 2
    print(s.findSum(2, 2, [5, 4, 3, 2, 1]))               # -> 170
    # Example 3
    print(s.findSum(1, 1, [28]))                          # -> 28

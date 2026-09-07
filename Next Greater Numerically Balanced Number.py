# Problem: 2048. Next Greater Numerically Balanced Number
# Problem Intuition:
#   We need to find the smallest integer greater than 'n' such that
#   for every digit 'd' in the number, it appears exactly 'd' times.
#   For example:
#       22 -> '2' appears 2 times (balanced)
#       1333 -> '1' appears once, '3' appears 3 times (balanced)
#       122333 -> 1->1×, 2->2×, 3->3× (balanced)
#   Such numbers are rare and irregularly spaced, so we can’t derive them
#   from a mathematical pattern. The safest approach is to test each next number.

# Solution Intuition:
#   - Start checking from n+1 since we need a strictly greater number.
#   - For each number, check if it's "numerically balanced":
#         * Convert to string
#         * For every unique digit 'd', count its occurrences
#         * If the count matches the digit itself for all digits, it’s balanced
#   - The moment we find one that satisfies this, return it.
#   - This approach is fast enough because balanced numbers occur below 10^7,
#     and checking each number’s digits is very quick.

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # Helper function to check if a number is numerically balanced
        def is_balanced(x: int) -> bool:
            s = str(x)
            # Check each unique digit in the number
            for ch in set(s):
                # Each digit 'd' must appear exactly 'd' times
                if s.count(ch) != int(ch):
                    return False
            return True

        num = n + 1  # Start from the next integer after n
        # Iterate upwards until a balanced number is found
        while True:
            if is_balanced(num):
                return num  # Return the first balanced number greater than n
            num += 1  # Otherwise, keep checking the next number

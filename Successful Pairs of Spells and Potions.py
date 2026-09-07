# Problem 2300: Successful Pairs of Spells and Potions
# Given two arrays: spells[] and potions[], and an integer success,
# count for each spell how many potions form a successful pair (spell * potion ≥ success).
# Return an array where each element corresponds to the count for each spell.
# Constraints: 1 ≤ n, m ≤ 10^5; 1 ≤ spells[i], potions[i] ≤ 10^5; 1 ≤ success ≤ 10^10


from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = len(potions)
        n = len(spells)
        pairs = []
        potions.sort()
        z = 0
        for i in range(n):
            y = success / spells[i]
            x = bisect.bisect_left(potions, y)
            z = m - x
            pairs.append(z)
        return pairs

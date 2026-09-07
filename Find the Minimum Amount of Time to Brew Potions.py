"""
LeetCode Problem 3494: Find the Minimum Amount of Time to Brew Potions
Difficulty: Medium

You are given two integer arrays:
- skill: length n, where skill[i] is the brewing speed of the ith wizard
- mana: length m, where mana[j] is the mana capacity of the jth potion

Each potion must be brewed in order and passed through all wizards sequentially.
The time taken by wizard i on potion j is: time[i][j] = skill[i] * mana[j]

Constraints:
- A potion must be passed to the next wizard immediately after the current wizard finishes.
- Wizards cannot start brewing a potion until the previous potion is fully brewed.
- Synchronization is required: each wizard starts exactly when the potion arrives.

Goal:
Return the minimum total time required to brew all potions properly.

Examples:
Input: skill = [1,5,2,4], mana = [5,1,4,2]
Output: 110

Input: skill = [1,1,1], mana = [1,1,1]
Output: 5

Input: skill = [1,2,3,4], mana = [1,2]
Output: 21
"""

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n=len(skill)
        f=[0]*n
        for x in mana:
            now=f[0]
            for i in range(1,n):
                now=max(now+skill[i-1]*x,f[i])
            f[n-1]=now+skill[n-1]*x
            for i in range(n-2,-1,-1):
                f[i]=f[i+1]-skill[i+1]*x
        return f[-1]
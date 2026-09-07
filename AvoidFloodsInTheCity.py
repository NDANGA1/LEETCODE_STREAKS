"""
Leetcode 1488: Avoid Flood in The City

Each day:
- rains[i] > 0 → rain fills lake rains[i]; if already full → flood
- rains[i] == 0 → dry any one lake to prevent future flood

Goal:
Return an array `ans`:
- -1 for rainy days
- lake number for dry days
- [] if flood is unavoidable

Strategy:
Track full lakes and schedule dry days to empty them before repeat rain.
Use binary search to assign dry days efficiently.
"""

from bisect import bisect_right


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        last_filled_days = {}
        dry_days = []
        for day in range(n):
            lake = rains[day]
            if lake > 0:
                if lake in last_filled_days:
                    last_filled_day = last_filled_days[lake]
                    idx = bisect_right(dry_days, last_filled_day)
                    if idx == len(dry_days):
                        return []
                    dry_day = dry_days.pop(idx)
                    ans[dry_day] = lake
                last_filled_days[lake] = day
            else:
                dry_days.append(day)
                ans[day] = 1
        return ans









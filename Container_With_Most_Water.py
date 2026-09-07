"""
Problem Summary:
Given an array 'height' of length n, where each element represents the height of a vertical line at position i,
find two lines that, together with the x-axis, form a container that holds the maximum amount of water.

The container's area is determined by the shorter of the two lines and the distance between them.
You may not slant the container—only vertical lines are allowed.

Goal:
Return the maximum area of water that can be trapped between any two lines.

Examples:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Input: height = [1,1]
Output: 1

Constraints:
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
"""


class Solution:
    def maxArea(self, height) -> int:
        n=len(height)
        xl=0
        xr=n-1
        yl=height[xl]
        yr=height[xr]
        x=abs(xl-xr)
        y=min(yl,yr)
        maxim=x*y
        for p in range(n-2):
            if yl==min(yl,yr):
                xi=xl+1
                yi=height[xi]
                yl,xl=yi,xi
            else:
                xi=xr-1
                yi=height[xi]
                yr,xr=yi,xi
            area=abs(xl-xr)*min(yl,yr)
            maxim=max(maxim,area)
        return maxim










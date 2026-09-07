nums=[2,2,3,4]
counter=0
nums.sort()
for i in range(len(nums)):
    y = i + 1
    k = y + 1
    for x in range(len(nums)-i-2):
        if nums[i]+nums[k]>nums[y] :

            counter+=1
            print(f"[{nums[i],nums[k],nums[y]}]")
        y += 1
        k += 1
print(" ")
print(f"...there are {counter} triangle triplets...")



from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: # Not enough elements to form a triangle
            return 0

        nums.sort() # Step 1: Sort the array

        count = 0
        # Loop for the first side (nums[i])
        for i in range(n - 2): # i can go up to n-3, leaving at least two elements for j and k
            # Side lengths must be positive. If nums[i] is 0, it cannot be part of a valid triangle.
            if nums[i] == 0:
                continue

            # Loop for the second side (nums[j])
            for j in range(i + 1, n - 1): # j goes from i+1 up to n-2, leaving at least one element for k
                # Loop for the third side (nums[k])
                for k in range(j + 1, n): # k goes from j+1 up to n-1
                    # Since the array nums is sorted (nums[i] <= nums[j] <= nums[k]),
                    # we only need to check one triangle inequality condition:
                    # nums[i] + nums[j] > nums[k]
                    # The other two conditions (nums[i] + nums[k] > nums[j] and nums[j] + nums[k] > nums[i])
                    # are automatically satisfied because nums[k] is the largest side.
                    if nums[i] + nums[j] > nums[k]:
                        count += 1
                    # Optimization: If nums[i] + nums[j] is not greater than nums[k],
                    # then for any subsequent k' (where k' > k), nums[k'] will be
                    # greater than or equal to nums[k]. This means nums[i] + nums[j]
                    # will also not be greater than nums[k'].
                    # So, we can break out of this innermost loop.
                    else:
                        break # This break significantly prunes the search space
                              # but the worst-case complexity remains O(N^3).
        return count


nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3
nums1[m:] = nums2
idx1=m+n-1
idx2=idx1-1
ptr1=nums1[idx1]
ptr2=nums1[idx2]
for i in range(m + n - 1):
    if ptr1 > ptr2:
        temp = ptr1
        ptr1 = ptr2
        ptr2 = temp
print(nums1)



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        idx2 = m + n - 1
        idx1 = idx2 - 1

        for i in range(m + n - 1):
            ptr1 = nums1[idx1]
            ptr2 = nums1[idx2]
            if ptr1 > ptr2:
                temp = ptr2
                nums1[idx2] = ptr1
                nums1[idx1] = temp
            idx1 -= 1
            idx2 -= 1
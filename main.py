
nums1=[1,2,3,0,0,0]
nums2=[2,5,6]

def merge(nums1, m: int, nums2, n: int):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1 =nums1
    nums1=nums1[:m]+nums2
    for i in range(m+n-1):
        for i in range(m+n-1):
            if nums1[i]>nums1[i+1]:
                temp=nums1[i]
                nums1[i]=nums1[i+1]
                nums1[i+1]=temp
    return nums1

print(merge(nums1,3,nums2,3))
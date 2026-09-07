
def triangleNumber(nums) -> int:
    n=len(nums)
    if n<3:
        return 0
    nums.sort()
    count=0
    for i in range(n-2):
        if nums[i]==0:
            continue
        j=i+1
        k=i+2
        for j in range (i+1,n-1):
            while k<n and nums[i]+nums[j]>nums[k]:
                k+=1
            count+=max(0,k-(j+1))
    return count

print(triangleNumber([4,2,3,4]))

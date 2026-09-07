nums=[2,2,3,4]
counter=0
for i in range(len(nums)):
    for k in range(len(nums)):
        for y in range(len(nums)):
            if i==k or i==y or y==k:
                continue
            if nums[i]+nums[k]>nums[y] and nums[i]+nums[y]>nums[k] and nums[y]+nums[k]>nums[i]:
                if nums[i]<=nums[k]<=nums[y]:
                    counter+=1
                    print(f"[{nums[i],nums[k],nums[y]}]")
print(" ")
print(f"...there are {counter} triangle triplets...")


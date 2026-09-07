nums=[[0,0],[0,1],[1,0],[0,2],[2,0]]
nums.sort(key=lambda x:x[0])
firstx=nums[0]
lastx=nums[-1]
nums.sort(key=lambda x:x[1])
firsty=nums[0]
lasty=nums[-1]
print(0.5*lastx[0]*lasty[1])


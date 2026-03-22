#eg nums=[1,3,4,5,7], target = 9
def getTarget(nums,target):
    left=0
    right=len(nums)-1
    while left<=right:
        sum=nums[left]+nums[right]
        if sum<target:
            left+=1
        if sum>target:
            right-=1
        if sum==target:
            return [nums[left],nums[right]]
    return -1 # Returns -1 if solution doesnt exist in the array
ans=getTarget([1,3,4,5,7],20)
print(ans)
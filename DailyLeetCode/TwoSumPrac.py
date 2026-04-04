def twoSum(nums,target):
    nums.sort()
    left=0
    right=len(nums)-1
    while left<right:
        total=nums[left]+nums[right]
        if total>target:
            right-=1
        elif total<target:
            left+=1
        else:
            return [nums[left],nums[right]]
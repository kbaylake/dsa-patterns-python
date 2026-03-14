#When order is preserved 
def moveZeros(nums):
    left=right=len(nums)-1
    while right >0:
        if nums[right]!=0:
            nums[left], nums[right] = nums[right], nums[left]
            left-=1
        right-=1
    print(left,right)
    for i in range(0,left+1):
        nums[i]=0
    return nums
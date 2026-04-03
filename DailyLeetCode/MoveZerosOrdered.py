#When order is preserved 
def moveZeros(nums):
    left=0
    pos=0
    for left in range(len(nums)):
        if nums[left]!=0 and nums[left+1]==0:
            nums[left+1]=nums[left]
            pos+=1
    for i in range(pos):
        nums[i]=0
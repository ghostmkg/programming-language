def quick_sort(nums, start, end): 
    if start>=end:
        return nums 
    p=pos(nums,start,end)
    quick_sort(nums,start,p-1)
    quick_sort(nums,p+1,end)
    return nums
def pos(nums,start,end):
    p=start-1 
    pivot=nums[end]
    for i in range(start,end):
        if pivot>nums[i]:
            p+=1
            nums[p],nums[i]=nums[i],nums[p]
    nums[end],nums[p+1]=nums[p+1],nums[end]
    return p+1
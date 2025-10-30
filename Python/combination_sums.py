def combinationSum(nums, target):
    res = []

    def tracking(temp, sum_, i):
        if i >= len(nums):
            return
        if sum_ > target:
            return
        if sum_ == target:
            res.append(temp)
            return
        

        tracking(temp + [nums[i]], sum_ + nums[i], i)
        tracking(temp, sum_, i+1)
    
    tracking([],0,0)

    return res

def getMaximumValue(weights, values, n, maxWeight):
    memo = {}
    def helper(weights,values,maxWeight,i):
        if maxWeight == 0:
            return 0
        if i >= n:
            return 0
        if (maxWeight,i) in memo:
            return memo[(maxWeight,i)]
        case1 = 0
        if(maxWeight - weights[i] >= 0):
            case1 = values[i]+helper(weights,values,maxWeight - weights[i],i)
        case2 = helper(weights,values,maxWeight,i+1)
        ans = max(case1,case2)
        memo[(maxWeight,i)] = ans
        return ans
    return helper(weights,values,maxWeight,0)
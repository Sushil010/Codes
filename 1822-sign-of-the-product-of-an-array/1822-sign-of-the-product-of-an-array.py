class Solution(object):
    def arraySign(self, nums):
        mul=1
        for i in range(len(nums)):
            mul=mul*nums[i]
        if(mul>0):
            return(mul//mul)
        if(mul<0):
            return(mul//abs(mul))
        else:
            return(mul)
            
        
class Solution(object):
    def runningSum(self, nums):
        sums=0
        list1=[]
        for i in range(len(nums)):
            sums=sums+nums[i]
            list1.append(sums)
            
        return(list1)    
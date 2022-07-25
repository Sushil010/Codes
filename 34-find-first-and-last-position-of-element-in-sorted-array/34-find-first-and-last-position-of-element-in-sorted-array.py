class Solution(object):
    def searchRange(self, nums, target):
        list3=[]
        if target in nums:
            for i in range(len(nums)):
                if (nums[i]==target):
                    list3.append(i)
                    break
        
            for j in reversed(range(len(nums))):
                if(nums[j]==target):
                    list3.append(j)
                    break
            
            return(list3)                
                
        else:
            return([-1,-1])
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
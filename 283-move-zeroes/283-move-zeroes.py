class Solution(object):
    def moveZeroes(self, nums):
        if (0 in nums):
            for i in range(len(nums)):
                nums.append(nums.pop(nums.index(0)))
        
        
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
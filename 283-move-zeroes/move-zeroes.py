class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c=0
        r=len(nums)
        for i in range(r):
            if nums[i]==0:
                c+=1
        while c>0:
            nums.append(0)
            nums.remove(0)
            c-=1
        
        
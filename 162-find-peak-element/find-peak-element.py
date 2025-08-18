class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)>0:
            return nums.index(max(nums))
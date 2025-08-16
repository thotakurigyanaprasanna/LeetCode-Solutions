class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target+1 in nums:
            return nums.index(target+1)
        elif target-1 in nums and target+1 not in nums:
            return nums.index(target-1)+1
        elif len(nums)<=1 and nums[0]>target:
            return 0
        elif target==0:
            return 0
        elif target>max(nums):
            return len(nums)
        elif target<min(nums):
            return 0
    
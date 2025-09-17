class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i]=p
            p*=nums[i]
        s=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=s
            s*=nums[i]
        return res


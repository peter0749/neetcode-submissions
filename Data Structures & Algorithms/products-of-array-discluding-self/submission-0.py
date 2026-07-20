class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fwd = [0] * len(nums)
        bwd = [0] * len(nums)
        ret = [0] * len(nums)
        fwd[0] = nums[0]
        bwd[-1] = nums[-1]
        for i in range(1, len(nums)):
            fwd[i] = fwd[i-1] * nums[i]
            bwd[len(nums)-i-1] = bwd[len(nums)-i] * nums[len(nums)-i-1]
        ret[0] = bwd[1]
        ret[-1] = fwd[-2]
        for i in range(1,len(nums)-1):
            ret[i] = fwd[i-1] * bwd[i+1]
        return ret
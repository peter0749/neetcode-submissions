class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = dict()
        for i, n in enumerate(nums):
            h[n] = i
        for i, n in enumerate(nums):
            if (target-n) in h and h[target-n] != i:
                return [i, h[target-n]]
        return None
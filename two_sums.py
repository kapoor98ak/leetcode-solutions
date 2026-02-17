class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r, n, res = 0, 0, len(nums), []
        for i in range(n-1):
            if target - nums[i] in nums[i+1:]:
                res = [i, nums.index(target - nums[i], i+1)]
                return res
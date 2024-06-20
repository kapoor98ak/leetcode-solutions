class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = len(nums)
        k %= l

        nums.reverse()

        nums[:k] = reversed(nums[:k])

        nums[k:] = reversed(nums[k:])

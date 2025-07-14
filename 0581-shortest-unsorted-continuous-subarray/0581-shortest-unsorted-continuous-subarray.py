class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sub_array = []
        sorted_nums = sorted(nums)
        if nums == sorted_nums:
            return 0
        lower, upper = len(nums)-1, 0
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                lower = min(lower, i)
                upper = max(upper, i)
        return 0 if lower >= upper else upper-lower+1
        
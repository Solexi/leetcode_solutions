class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        Sum, min_val = 0,0
        for i in nums:
            Sum += i
            min_val = min(min_val, Sum)
        return abs(min_val) + 1
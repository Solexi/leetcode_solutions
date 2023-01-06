class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_values = []
        for i, value in enumerate(nums):
            squared_values.append(value**2)
            squared_values.sort()
        return squared_values
            
        
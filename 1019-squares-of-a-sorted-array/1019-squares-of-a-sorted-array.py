class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            nums[i]*=nums[i]
            result.append(nums[i])
        result.sort()
        return result

        
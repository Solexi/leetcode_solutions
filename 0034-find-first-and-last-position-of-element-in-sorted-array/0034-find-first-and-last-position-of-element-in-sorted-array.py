class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = 0
        for i in range(len(nums)):
            if nums == []:
                return [-1, -1]
            if nums[i] == target:
                start = i
                for j in range(start, len(nums)):
                    if nums[j] == target:
                        end = j
                return [start, end]
        return [-1, -1]
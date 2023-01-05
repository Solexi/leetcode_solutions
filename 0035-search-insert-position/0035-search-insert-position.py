class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = 0
        while start < len(nums):
            if nums[start] == target:
                return start
                start+=1
            else:
                nums.append(target)
                nums.sort()
                return nums.index(target)
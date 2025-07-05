class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return
        for i in range(len(nums)):
            index = abs(nums[i])-1
            print(nums[i])
            print(index)
            if nums[index] < 0:
                return abs(nums[i])
            nums[index] = -nums[index]
        return -1

        
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concatVal = 0
        if nums == []:
            return
        while nums:
            if nums == []:
                return
            if len(nums) > 1:
                concatVal += int(str(nums[0]) + str(nums[-1]))
                nums.pop(0)
                nums.pop(-1)
            else:
                concatVal += nums[0]
                nums.pop(0)
        return concatVal

            
                
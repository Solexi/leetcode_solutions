class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
    
        # i = 0
        # count_k = 0
        # while i < len(nums):
        #     if nums[i] == val:
        #         nums.pop(i)
        #     else:
        #         count_k += 1
        #         i += 1
        # return count_k

                
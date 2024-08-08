class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sums = 0
        count = 0
        if nums == []:
            return 0
        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                sums += i
                count+=1
        if count != 0:
            aver = sums // count
            return aver
        else:
            return 0
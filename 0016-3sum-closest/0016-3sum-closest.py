class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sums = []
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                sums.append(sum)
                if sum == target:
                    return sum
                if sum < target:
                    left += 1
                else:
                    right -= 1   
        return sums[min(range(len(sums)), key = lambda x: abs(sums[x]-target))]

        
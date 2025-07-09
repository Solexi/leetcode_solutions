# Better Space Complexity

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(sum - target) < abs(closest_sum - target):
                    closest_sum = sum
                if sum == target:
                    return sum
                if sum < target:
                    left += 1
                else:
                    right -= 1   
        return closest_sum

        
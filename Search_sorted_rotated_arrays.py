def search(nums, target):
            # for x in nums:
        if not nums:
            return -1

        lo = 0 
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid

            if nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1
nums = [0,1,2,4,5,6]
print(search(nums, 4))
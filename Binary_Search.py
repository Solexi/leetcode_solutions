def search(nums, target):
        low = 0
        high = len(nums)-1

        while high - low > 1:
            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        if nums[low] == target:
            return(low)
        elif nums[high] == target:
            return(high)
        else: 
            return(-1)
nums = [-1,0,3,5,9,12]
target = 3
print(search(nums, target))


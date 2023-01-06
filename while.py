

def sum(nums, target):
    l = 0
    r = len(nums) - 1

    while l < r:
        if nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            return [nums[l], nums[r]]

    return None


print(sum([2, 3, 4, 5, 7], 20))

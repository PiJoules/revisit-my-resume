def sum_for(nums):
    s = 0
    for n in nums:
        s += n
    return s


def sum_while(nums):
    s = 0
    i = 0
    while i < len(nums):
        s += nums[i]
        i += 1
    return s


def sum_recursive(nums):
    if not nums:
        return 0
    else:
        return nums[0] + sum_recursive(nums[1:])

lst = list(range(5))

assert sum(lst) == sum_for(lst) == sum_while(lst) == sum_recursive(lst)

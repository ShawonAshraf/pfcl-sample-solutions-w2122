def product(nums):
    if len(nums) == 0:
        return 1
    return nums[0] * product(nums[1:])


def squares(nums):
    if len(nums) == 0:
        return []
    return [nums[0]**2] + squares(nums[1:])


def num_zeros(n):
    num_str = str(n)
    count = 0

    if len(num_str) == 0:
        return count
    if num_str[0] == "0":
        count += 1
    elif num_str[0] != "0":
        count += 0

    return count + num_zeros(num_str[1:])

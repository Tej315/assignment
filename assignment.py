nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
def remove_duplicates(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    
    for i in range(k, len(nums)):
        nums[i] = "_"
    return k
    if not nums:
        return 0
result_length = remove_duplicates(nums)
print("Output:", result_length, ", nums =", nums)
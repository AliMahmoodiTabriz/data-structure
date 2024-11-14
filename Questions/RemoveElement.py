from typing import List


def removeElement(nums: List[int], val: int) -> int:
    move_index = 0
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = "_"
        else:
            nums[move_index], nums[i] = nums[i], nums[move_index]
            move_index += 1

    return move_index


def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


def removeDuplicates2(nums: List[int]) -> int:
    if not nums:
        return 0
    write_index = 1
    count = 1
    for read_index in range(1, len(nums)):
        if nums[read_index] == nums[read_index - 1]:
            count += 1
        else:
            count = 1

        if count <= 2:
            nums[write_index] = nums[read_index]
            write_index += 1
    return write_index


nums = [0, 0, 0, 0, 1, 1, 1, 1, 2, 3, 3]
# nums = [1, 1, 1, 2, 2, 3]
# nums = [1, 1, 1]
# nums = [0, 0, 0, 0, 0]
# nums = [1, 2, 2, 2]
k = removeDuplicates2(nums)
print(nums[:k])

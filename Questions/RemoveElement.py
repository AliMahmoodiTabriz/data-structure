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


nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums)
print(nums)
print(k)

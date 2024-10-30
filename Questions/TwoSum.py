

def twoSum(nums: list[int], target: int) -> list[int]:
    my_map = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in my_map:
            return [my_map[need], i]
        my_map[num] = i
    
    return [-1, -1] 


print(twoSum([3, 3], 6))

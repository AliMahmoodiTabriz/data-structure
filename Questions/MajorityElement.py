def majorityElement(nums: list[int]) -> int:
    my_dic = {}
    mid = len(nums) // 2

    for num in nums:
        my_dic[num] = my_dic.get(num, 0) + 1
        if my_dic[num] > mid:
            return num 

def MajorityElement(nums: list[int]) -> int:
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate

arr = [3, 2, 3]
arr1 = [2, 2, 1, 1, 1, 2, 2]
arr2 = [1]
print(majorityElement(arr))
print(majorityElement(arr1))
print(majorityElement(arr2))
print("-----------------------")
print(MajorityElement(arr))
print(MajorityElement(arr1))
print(MajorityElement(arr2))
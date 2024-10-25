from typing import List


def validateMounainArr(arr: List[int]) -> bool:
    i = 1
    while i < len(arr) and arr[i] > arr[i-1]:
        i += 1
    if i == 1 or i == len(arr):
        return False
    while i < len(arr) and arr[i] < arr[i-1]:
        i += 1
    return i == len(arr)

arr=[1,2,3,4,3,2,1]
print(validateMounainArr(arr))

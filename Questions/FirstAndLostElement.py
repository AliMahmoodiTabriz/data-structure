
# def serchRange(arr: list[int], val) -> list[int]:
#     left = 0
#     right = len(arr) - 1

#     while left > -1 and left < len(arr)-1:
#         if arr[left] != val:
#             left += 1
#         if arr[right] != val:
#             right -= 1
#         if arr[left] == val and arr[right] == val:
#             return [left, right]
#     return []
def serchRange(arr: list[int], val) -> list[int]:
    left = searchOnLeft(arr, val)
    right = searchOnRight(arr, val)
    return [left, right]


def searchOnLeft(arr: list[int], val) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = int((right + left) / 2)
        if arr[mid] == val:
            if mid == 0 or arr[mid - 1] != val:
                return mid
            right = mid-1
        elif arr[mid] > val:
            right = mid-1
        else:
            left = mid+1

    return -1


def searchOnRight(arr: list[int], val) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = int((right + left) / 2)
        if arr[mid] == val:
            if mid == len(arr)-1 or arr[mid + 1] != val:
                return mid
            left = mid +1
        elif arr[mid] > val:
            right = mid -1
        else:
            left = mid +1

    return -1


print(serchRange([5,7,7,8,8,10], 11))

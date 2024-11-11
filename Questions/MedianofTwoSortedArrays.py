from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    merged = merge(nums1, nums2)
    if len(merged) % 2 == 0:
        return (merged[len(merged)//2] + merged[(len(merged)//2) - 1]) / 2
    
    return merged[len(merged)//2]


def merge(first_list, last_list):
    combined = []
    i, j = 0, 0
    
    while i < len(first_list) and j < len(last_list):
        if first_list[i] < last_list[j]:
            combined.append(first_list[i])
            i += 1
        else:
            combined.append(last_list[j])
            j += 1
    
    combined.extend(first_list[i:])
    combined.extend(last_list[j:])
    
    return combined
[1,2,3]
nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1,nums2))
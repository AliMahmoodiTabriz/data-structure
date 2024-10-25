from typing import List


class MergeSortedArray:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m-1, n-1, m+n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


my_merge = MergeSortedArray()
num1 = [1, 2, 3, 0, 0, 0]
num2 = [2, 5, 6]
my_merge.merge(num1, 3, num2, 3)

print(num1)

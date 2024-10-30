def minimumMountainRemovalsNsqure(nums):
    n = len(nums)

    # Step 1: Calculate left (longest increasing subsequence up to each index)
    left = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                left[i] = max(left[i], left[j] + 1)

    # Step 2: Calculate right (longest decreasing subsequence from each index)
    right = [1] * n
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                right[i] = max(right[i], right[j] + 1)

    # Step 3: Find maximum mountain length
    max_mountain_len = 0
    for i in range(1, n - 1):
        if left[i] > 1 and right[i] > 1:  # Valid peak
            max_mountain_len = max(max_mountain_len, left[i] + right[i] - 1)

    # Step 4: Minimum removals to make the array a mountain
    return n - max_mountain_len
def minimumMountainRemovals(nums):
    import bisect

    n = len(nums)

    # En Uzun Artan Alt Dizi (LIS) uzunluklarını hesaplayan fonksiyon
    def calculate_LIS(sequence):
        dp = []
        lis_lengths = [0] * len(sequence)
        for i, num in enumerate(sequence):
            idx = bisect.bisect_left(dp, num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
            lis_lengths[i] = idx + 1
        return lis_lengths

    # Soldan sağa LIS hesapla
    lis = calculate_LIS(nums)
    # Sağdan sola LIS (LDS) hesapla
    lds = calculate_LIS(nums[::-1])[::-1]

    max_mountain_len = 0
    for i in range(1, n - 1):
        if lis[i] > 1 and lds[i] > 1:
            mountain_len = lis[i] + lds[i] - 1
            max_mountain_len = max(max_mountain_len, mountain_len)

    return n - max_mountain_len

print(minimumMountainRemovals([1, 2, 1, 3, 4, 3, 1, 2, 2]))  # Çıktı: 3
print(minimumMountainRemovals([1, 16, 84, 9, 29, 71, 86, 79, 72, 12]))  # Çıktı: 2
print(minimumMountainRemovals([1, 2, 3, 4, 4, 3, 2, 1]))  # Çıktı: 1
print(minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1]))  # Çıktı: 3
print(minimumMountainRemovals([4, 3, 2, 1, 1, 2, 3, 1]))  # Çıktı: 4
print(minimumMountainRemovals([1, 3, 1]))  # Çıktı: 0

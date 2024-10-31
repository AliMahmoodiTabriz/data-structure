def MissingNumber(nums: list[int]) -> int:
    n = len(nums)
    sigma = int(n * (n+1) / 2)
    total = 0
    for i in range(n):
        total += nums[i]
    return sigma - total


print(MissingNumber([0, 1, 2, 3, 4, 5, 6, 7]))

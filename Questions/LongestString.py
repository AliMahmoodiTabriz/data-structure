def lengthOfLongestSubstring(arr: list[chr]) -> int:
    if len(arr) <= 1:
        return len(arr)

    L = 0
    R = 0
    longest = 0
    seenChcacter = {}
    while L < len(arr) and R < len(arr):
        currentCharacter = arr[R]
        if currentCharacter in seenChcacter:
            preveCharacterPos = seenChcacter[currentCharacter]
            L = max(L, preveCharacterPos + 1)
        seenChcacter[currentCharacter] = R
        longest = max(longest, R-L + 1)
        R += 1
    return longest


print(lengthOfLongestSubstring(['a', 'b', 'c', 'a', 'b', 'c', 'a']))

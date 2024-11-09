def convert(s: str, numRows: int) -> str:
    lsStr = [""] * numRows
    temp = numRows
    r = 0
    i = 0
    if numRows == 1:
        return s
    while i <= len(s)-1:
        lsStr[r] += s[i]
        if r < temp-1:
            r += 1
        else:
            if r == 0:
                temp = numRows
                r = 1
            else:
                r -= 1
                temp -= 1
        i += 1
    result = ""
    for item in lsStr:
        result += item
    return result


print(convert("AB", 1))

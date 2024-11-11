def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    lsStr = [""] * numRows
    r = 0
    going_down = True
    for item in s:
        lsStr[r] += item

        if r == 0:
            going_down = True
        elif r == numRows - 1:
            going_down = False

        r += 1 if going_down else -1
        item

    return "".join(lsStr)


responce = convert("PAYPALISHIRING", 3)
if responce == "PAHNAPLSIIGYIR":
    print(responce)
else:
    print("is wrong")    
    

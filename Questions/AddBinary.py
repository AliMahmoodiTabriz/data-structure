def AddBinary(a: list[int], b: list[int]) -> str:
    i = len(a)-1
    j = len(b)-1
    carry = 0
    result = ""
    while i >= 0 or j >= 0 or carry == 1:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        result = str(carry % 2) + result
        carry //= 2
    return result

print(AddBinary('1111','1101'))

def myAtoi(s: str) -> int:
    min_32bit = -2**31
    max_32bit = 2**31 - 1
    
    s = s.lstrip()
    
    if not s:
        return 0
    
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    
    result = 0
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break
    
    result *= sign
    
    if result < min_32bit:
        return min_32bit
    elif result > max_32bit:
        return max_32bit
    else:
        return result

# Test örnekleri
print(myAtoi("1"))
print(myAtoi("1340"))
print(myAtoi("42"))            # 42
print(myAtoi("   -042"))       # -42
print(myAtoi("1337c0d3"))      # 1337
print(myAtoi("0-1"))           # 0
print(myAtoi("words and 987")) # 0
def reverse(x: int) -> int:
    # İşareti kontrol et ve pozitif hale getir
    sign = -1 if x < 0 else 1
    x = abs(x)
    
    # Sayıyı ters çevir
    reversed_x = int(str(x)[::-1]) * sign
    
    # int32 sınırını kontrol et
    int32_min = -2_147_483_648
    int32_max = 2_147_483_647
    if reversed_x < int32_min or reversed_x > int32_max:
        return 0
    
    return reversed_x

# Test örnekleri
print(reverse(123))       # Output: 321
print(reverse(-123))      # Output: -321
print(reverse(120))       # Output: 21
print(reverse(1534236469)) # Output: 0



print(reverse(1534236469))

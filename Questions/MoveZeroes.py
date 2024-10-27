
def moveZeroes(arr: list[int]) -> list[int]:
    j = 0
    for item in arr:
        if item != 0:
            arr[j] = item
            j += 1

    for i in range(j,len(arr)):
        arr[i]=0    

  # i = 0
  # while i < len(arr)-1:
  #     if arr[i] == 0 and arr[i+1] != 0:
  #         arr[i], arr[i+1] = arr[i+1], arr[i]
  #         if i!=0:
  #          i -= 1
  #         continue
  #     i += 1

    return arr


arr = [0, 1]
moveZeroes(arr)
arr = [0,1,0,3,12]
moveZeroes(arr)
print(arr)

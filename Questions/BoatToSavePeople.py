import math
from typing import List


def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort()
    boats = 0
    left = 0
    right= len(people) -1
    while left <= right:
        if people[left] + people[right] <= limit:
            left +=1
            right -= 1
        else:
            right -= 1
        boats +=1    
    return boats

print(numRescueBoats([2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10], 50))
print(numRescueBoats([1, 1, 2, 3], 3))
print(numRescueBoats([1, 2, 3, 3], 5))

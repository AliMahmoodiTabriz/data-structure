import math
from typing import List


def numRescueBoats(people: List[int], limit: int) -> int:
        total_peaople=0
        for item in people:
            total_peaople += item
        return math.ceil(total_peaople / limit) 
    
    
    
print(numRescueBoats([1,2],3))    
print(numRescueBoats([3,2,2,1],3))    
print(numRescueBoats([3,5,3,4],5))
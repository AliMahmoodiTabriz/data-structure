# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= 5


def firstBadVersion(n: int) -> int:
    if n == 1:
        return n 
    L=1
    R=n
    while L < R:
        mid = int((L+R) / 2)
        if isBadVersion(mid):
            R=mid
        else:
           L= mid+1
    return L


print(firstBadVersion(20))

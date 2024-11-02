import math
def countPrimes(num: int) -> int:
    if num < 2:
        return [0]

    def isPrime(val, counter):
        if val <= 2:
            return counter

        calc = num % (val - 1)
        if calc == 0:
            return 0
        else:
            counter += 1
            return isPrime(val - 1, counter)

    return isPrime(num, 0)


def getPrimes(n: int):
    if n < 2:
        return 0
    prime = [True] * n
    prime[0] = prime[1] = False 

    for i in range(2, math.ceil(math.sqrt(n))):
        if prime[i]:
            for j in range(i * i, n, i):
                prime[j] = False

    count = sum(prime)
    return count


print(getPrimes(45))

def isPrime(x):
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt = cnt + 1
    if cnt == 2:
        return True
    return False

def filter_prime(nums):
    primes = [x for x in nums if isPrime(x)]
    return primes

inp1 = input().split()
inp2 = map(int, inp1)
print(filter_prime(inp2))
primes = [0, 0]
for i in range(2, 1001):
    is_prime = True
    for f in range(2, int(sqrt(i)) + 1):
        if i % f == 0:
            is_prime = False
    if is_prime:
        primes.append(i)
    else:
        primes.append(primes[-1])


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        prev = 0
        for n in nums:
            bound = n - prev
            if n - primes[bound - 1] <= prev:
                return False
            prev = n - primes[bound - 1]
        return True

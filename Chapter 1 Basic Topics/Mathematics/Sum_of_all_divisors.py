def sumOfDivisors(N):
    divisors_sum = 0
    for number in range(1, N + 1):
        divisors_sum += (N // number) * number
    return divisors_sum

def isPrime(N):
    count = 0
    num = 1
    while num * num <= N:
        if N % num == 0:
            count += 1
            if (N // num) != num:
                count += 1
        num += 1
    if count == 2:
        return 1
    else:
        return 0
                
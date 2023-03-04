def lcmAndGcd(A , B):
    A_clone = A
    B_clone = B
    # Euclidean Algoritm
    while A > 0 and B > 0:
        if A > B:
            A = A % B
        else:
            B = B % A
        if A == 0:
            gcd = B
        else:
            gcd = A
    lcm = (A_clone * B_clone) // gcd
    return lcm, gcd

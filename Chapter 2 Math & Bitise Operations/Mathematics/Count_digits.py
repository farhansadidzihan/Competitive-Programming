def evenlyDivides(N):
    divider = 0
    for digit in str(N):
        if int(digit) > 0:
            if N % int(digit) == 0:
                divider += 1
    return divider

def reverse(x: int) -> int:
    reverse_num = 0
    while x > 0:
        last_num = x % 10
        reverse_num = (reverse_num * 10) + last_num
        x = x // 10
    
    if "-" in str(x):
        x = x - (x + x)
        while x > 0:
            last_num = x % 10
            reverse_num = (reverse_num * 10) + last_num
            x = x // 10
        return reverse_num - (2 * reverse_num)
    return reverse_num
    
def reversedBits(X):
    binary = '{:032b}'.format(X)
    binary = binary[ : : -1]
    decimal = int(binary, 2)
    return decimal

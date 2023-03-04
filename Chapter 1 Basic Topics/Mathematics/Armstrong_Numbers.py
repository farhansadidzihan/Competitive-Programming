def armstrongNumber (n):
    x = n
    reverse_num = 0
    total = 0
    while x > 0:
        last_num = x % 10
        total = total + (last_num ** 3)
        reverse_num = (reverse_num * 10) + last_num
        x = x // 10
    reversed_num = reverse_num
    # Conditions
    if n == total:
        return "Yes"
    elif "-" in str(n):
        return "Yes"
    else:
        return "No"

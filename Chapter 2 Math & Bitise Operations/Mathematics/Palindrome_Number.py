def is_palindrome(n):
    x = n
    reverse_num = 0
    while x > 0:
        last_num = x % 10
        reverse_num = (reverse_num * 10) + last_num
        x = x // 10
    reversed_num = reverse_num
    # Conditions
    if n == reversed_num:
        return "Yes"
    elif "-" in str(n):
        return "Yes"
    else:
        return "No"

# || =====\\ Linear Search is a Searching Algorithm //===== ||

# || The Time Complexity of Linear Search is O(n) || Linear Search is also called Sequencial/Simple Search ||

# || 01 ||

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def Linear_Search(list, x):
    length = len(list)
    i = 0
    
    while i < length:
        if list[i] == x:
            return f"The number is on {i} index"
        i += 1

    else:
        i = -1 
        print(f"Sorry! The Number is not in this List.")

if __name__ == "__main__":
    try:
        user_input = int(input("Enter your number:-"))
    except ValueError as e:
        print("Please, Enter a Valid Value!")

    print(Linear_Search(list, user_input))

# || 02 ||

list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def Linear_Search(list, n):
    for i in range(0, len(list)):
        if list[i] == n:
            return f"{n} is on {i} index"
    else:
        return f"Sorry! {n} is not in list"

if __name__ == "__main__":
    user_input = int(input("Enter a number\n:-"))
    print(Linear_Search(list, user_input))
    
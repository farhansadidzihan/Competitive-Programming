# || =====\\ Binary Search is a Popular Searching Algorithm //===== ||

# || The Time Complexity of Binary Search is O(log n) || Binary Search is Better approch than Linear Search ||

# || 01 ||

def Binary_Search(list, n):
    left, right = 0, len(list) - 1 
    
    while left <= right:
        mid = (left + right) // 2 
        if list[mid] == n:
            return mid

        if list[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

if __name__ == "__main__":
    user_input = int(input("Enter Your Number\n:-"))
    position = Binary_Search(list, user_input)
    if position == -1:
        if user_input in list:
            print(f"{user_input} is in list, but function returned -1")
        else:
            print(f"{user_input} not in list")
    else:
        if list[position] == user_input:
            print(f"{user_input} found in correct position.")
        else:
            print(f"Binary Search returned {position} for {user_input} which is incorrect")

# || 02 ||

def Binary_Search(list, n):
    first = 0
    last  = len(list) - 1 
    
    while first <= last:
        mid_point = (first + last) // 2
        
        if list[mid_point] == n:
            return f"{n} is found on {mid_point} index"
        elif list[mid_point] < n:
            first = mid_point + 1
        else:
            last = mid_point - 1
    
    else:
        return f"{n} is not found in the list"

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

try:
    user_input = int(input("Enter a number\n:-"))
    print(Binary_Search(list, user_input))
except Exception as e:
    print("Please, Enter a valid value!")

# || 03 || Binary Search With Recursion ||

def Recursive_Binary_Search(list, n):
    if len(list) == 0:
        return False
    else:
        mid_point = (len(list)) // 2
        
        if list[mid_point] == n:
            return f"{n} is found in this list"
        else:
            if list[mid_point] < n:
                return Recursive_Binary_Search(list[mid_point + 1 : ] , n )
            else:
                return Recursive_Binary_Search(list[ : mid_point] , n )
    
        
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

while True:
    try:
        num = int(input("Enter a number\n:-"))
        print(Recursive_Binary_Search(li, num))
    except Exception as e:
        print("Please, Enter a valid value!")

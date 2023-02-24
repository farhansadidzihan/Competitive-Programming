# || =====\\ Array is a Linear & Static Data Structure //===== ||

# || Array can be Homogeneous or Non-Homogeneous in different Programming Languages ||
# || Python doesn't have Array, but the bult-in data sturcture of Python, called List is made by Array || PyList is Non-Homogeneous ||

# || Array is an index based Data Stucture, So the Accessing Complexity of Array or Pylist is O(1) ||
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list.append(10)
list[9] = 10
list.pop()
print(f"{list[0 : ]} lenght of the list is:- {len(list)}")

# || Searching Complexity of Array or Pylist with Linear Search is O(n) ||
def Linear_Search_in_Array_or_Pylist(list, n):
    for i in range(0, len(list)):
        if list[i] == n:
            return f"{n} is on {i} index"
    else:
        return f"Sorry! {n} is not in list"
user_input = int(input("Enter a number\n:-"))
print(Linear_Search_in_Array_or_Pylist(list, user_input))

# || Searching Complexity of Array or Pylist with Binary Search is O(log n) ||
def Binary_Search_in_Array_or_Pylist(list, n):
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
user_input = int(input("Enter a number\n:-"))
print(Binary_Search_in_Array_or_Pylist(list, user_input))

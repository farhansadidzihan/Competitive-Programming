# || =====\\ Merge Sort is one of the Most Popular Sorting Algorithm //===== ||

# || In Merge Sort, At First We divide the list into two sub-list then, We sort them differently and After sorting both sub-lists, We merge the sub-lists || This typical algorithms are called "Divide and Conquer" ||
# || The Time Complexity of Dividing part is O(log n) & Merging part is O(n) || So, The Time Complexity of the whole Algorithm is O(n log n) ||

# || 01 ||
def split(list):
    mid = len(list) // 2
    left = list[ : mid]
    right = list[mid : ]
    return left, right

def merge(left_list, right_list):
    li = []
    i, j = 0, 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            li.append(left_list[i])
            i += 1
        else:
            li.append(right_list[j])
            j += 1
    while i < len(left_list):
        li.append(left_list[i])
        i += 1
    while j < len(right_list):
        li.append(right_list[j])
        j += 1
    return li

def merge_sort(list):
    ''' Sorts a list in order & returns a new sorted list '''
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)

if __name__ == "__main__":
    unsorted_list = [30, 10, 25, 15, 70]
    merge_sort(unsorted_list)
    print(unsorted_list)
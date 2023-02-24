# || =====\\ Quick Sort is one of the Most Popular Sorting Algorithms //===== ||

# || In Quick Sort, At First We select a number from the list, that's called "Pivot". Put the Pivot and put all lesser nubers in left & greater numbers in right side of the Pivot . This is called "Partison"||
# || This is "Divide and Conquer" type Algorithm || The Time Complexity of the Partison is O(n) & Diving is O(log n) || So, The Time Complexity of the whole Algorithm is O(n log n), but worst case it takes O(n^2) ||

# || 01 ||
def quick_sort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1 : ]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    # print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot)) # With Debug Output 
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

if __name__ == "__main__":
    unsorted_list = [30, 10, 25, 15, 70]
    quick_sort(unsorted_list)
    print(unsorted_list)

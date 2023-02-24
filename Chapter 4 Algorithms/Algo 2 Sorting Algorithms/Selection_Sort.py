# || =====\\ Selection Sort is Sorting Algorithm //===== ||

# || 01 ||
def selection_sort(list):
    n = len(list)
    for i in range(0, n - 1):
        index_min = i
        for j in range(i + 1, n):
            if list[j] < list[index_min]:
                index_min = j
        if index_min != i:
            list[i], list[index_min] = list[index_min], list[i]
            print(list, "--> ", end = "")

if __name__ == "__main__":
    unsorted_list = [30, 10, 25, 15, 70]
    selection_sort(unsorted_list)
    print(unsorted_list)

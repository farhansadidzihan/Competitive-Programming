# || =====\\ Insertion Sort is Sorting Algorithm //===== ||

# || 01 ||
def insertion_sort(list):
    n = len(list)
    for i in range(1, n):
        item = list[i]
        j = i - 1
        while j >= 0 and list[j] > item:
            list[j + 1] = list[j]
            j = j - 1
            list[j + 1] = item
            print(list, "--> ", end = "")

if __name__ == "__main__":
    unsorted_list = [30, 10, 25, 15, 70]
    insertion_sort(unsorted_list)
    print(unsorted_list)

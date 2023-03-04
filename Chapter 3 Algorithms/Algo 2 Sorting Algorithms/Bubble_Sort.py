# || =====\\ Bubble Sort is Sorting Algorithm //===== ||

# || 01 ||
def bubble_sort(list):
    n = len(list)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                print(list, "--> ", end = "")

if __name__ == "__main__":
    unsorted_list = [30, 10, 25, 15, 70]
    bubble_sort(unsorted_list)
    print(unsorted_list)

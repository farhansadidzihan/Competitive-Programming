# || =====\\ Heap is a Complete Binary Tree, in which Every Node is greater or less than it's Child Node //===== ||

# || In Heap, if The Value of Each Node is Greater Than it's Child Node is called "Max Heap" & Less Than it's Child Node is "Min Heap" ||

# || 01 || Max Heap ||
def left(i):
    return 2 * i

def right(i):
    return 2 * i

def parent(i):
    return i // 2

def is_max_heap(H):
    n = len(H) - 1
    for i in range(n, 1, -1):
        p = parent(i)
        if H[p] < H[i]:
            return False
        else:
            return True
if __name__ == "__main__":
    H = [None, 19, 7, 17, 3, 5, 12, 10, 1, 2] 
    print(f"{H} is Max Heap {is_max_heap(H)}")

def max_heapify(heap, heap_size, i):
    l = left(i)
    r = right(i)
    if l <= heap_size and heap[l] > heap[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and heap[r] > heap[largest]:
        largest = r
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, heap_size, largest)
if __name__ == "__main__":
    h = [None, 19, 7, 17, 3, 5, 12, 10, 1, 2]
    print(h)
    max_heapify(h, 9, 3)
    print(h)

def build_max_heap(heap):
    heap_size = len(heap) - 1
    for i in range(heap_size // 2, 0, -1):
        max_heapify(heap, heap_size, i)
if __name__ == "__main__":
    heap = [None, 19, 7, 17, 3, 5, 12, 10, 1, 2]
    print(f"Before Building Heap {heap}")
    build_max_heap(heap)
    print(f"After Building Heap {heap}")

# || Heap Sort ||
def heap_sort(heap):
    build_max_heap(heap)
    heap_size = len(heap) - 1
    for i in range(heap_size, 1, -1):
        heap[1], heap[i] = heap[i], heap[1]
        heap_size -= 1
        max_heapify(heap, heap_size, 1)
if __name__ == "__main__":
    heap = [None, 19, 7, 17, 3, 5, 12, 10, 1, 2]
    print(f"Before Sorting Heap :-{heap}")
    heap_sort(heap)
    print(f"After Sorting Heap :-{heap}")
    
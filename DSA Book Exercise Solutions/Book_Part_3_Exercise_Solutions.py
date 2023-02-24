# || Python Die Programming Shekha Part 3 || Data Sturctures and Algorithms || Exersice part Solutions ||

# || Exersice of Unit 02 || Time & Space Complexity ||

# Exercise no.01
n = int(input())
count = 0
for i in range(n):  # Page no 23
    count += 1
print(f"n = {n} count = {count}")  # The Coplexity of This Programme is O(n)

# Exercise no.02
  # Not Codeable // Exercise of Page no.25

# Exercise no.03
n = int(input())
count = 0
for i in range(n):
    count += 1
for i in range(n):
    for j in range(n):
        count += 1
print(count)  # The Coplexity of This Programme is O(n^2)

# || Exersice of Unit 05 || Sorting Algorithm ||

# Exercise no.01
def selection_sort(L):
    n = len(L)
    for i in range(0, n - 1):
        index_min = i
        for j in range(i + 1, n):
            if L[j] < L[index_min]:
                index_min = j
            
        if index_min != i:
            L[i], L[index_min] = L[index_min], L[i]  # Page no.45

if __name__ == "__main__":
    L = [8, 2, 4, 1, 5, 7]
    selection_sort(L)
    print(L)

# Exercise no.02
def bubble_sort(L):
    n = len(L)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]  # Page no.50

if __name__ == "__main__":
    L = [3, 1, 7, 6, 2]
    bubble_sort(L)
    print(L)

# Exercise no.03
def bubble_sort(L):
    n = len(L)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]  # Page no.52
                print(L, "--> ", end = "")  # Changed To Print Step By Step

if __name__ == "__main__":
    L = [3, 1, 7, 6, 2]
    bubble_sort(L)
    print(L)

# Exercise no.04
  # Cannot Solved // Exercise of Page no.52

# Exercise no.05
def insertion_sort(list):
    n = len(list)
    for i in range(1, n):
        item = list[i]
        j = i - 1
        while j >= 0 and list[j] > item:  # Page no.56
            list[j + 1] = list[j]
            j = j - 1
            list[j + 1] = item

if __name__ == "__main__":
    L = [5, 4, 3, 2, 1]
    insertion_sort(L)
    print(L)

# Exercise no.06
def insertion_sort(list):
    n = len(list)
    for i in range(1, n):
        item = list[i]
        j = i - 1
        while j >= 0 and list[j] > item:  # Page no.56
            list[j + 1] = list[j]
            j = j - 1
            list[j + 1] = item

if __name__ == "__main__":
    L = [1, 2, 3, 4, 5]
    insertion_sort(L)
    print(L)

# || Exersice of Unit 06 || Stack & Queue ||

# Exercise no.01
def is_balanced(input_str):
    s = list()
    
    for ch in input_str:
        if ch == "(" or ch == "{" or ch == "[":
            s.append(ch)
        if ch == ")" or ch == "}" or ch == "]":  # Page no.63
            if not s:
                return False
            s.pop()
    return not s

if __name__ == "__main__":
    while True:
        string = input("Check Your Brackets are balanced or not! \n:-")
        if is_balanced(string):
            print(f"{string} is balanced!")
        else:
            print(f"{string} is not balanced!")

# Exercise no.2
  # Not Codeable // Exercise of Page no.63

# || Exersice of Unit 07 || Linked List ||

# Exercise no.01
class Node:
    ''' An object for storing a single node of doubly linked list '''

    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)

class Doubly_Linked_List:
    ''' It's a Doubly linked list '''

    def __init__(self):
        self.head = Node()
    
    def __repr__(self):
        nodes = []
        current_node = self.head.next
        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next
        return "--> ".join(nodes)
    
    def append(self, data):
        node = Node(data)
        if self.head.next is None:
            self.head.next = node
            return
        current_node = self.head.next
        while current_node.next: # It means current_node.next is not None
            current_node = current_node.next
        current_node.next = node
        node.prev = current_node

    def prepend(self, data):
        first_node = self.head.next
        new_node = Node(data, None, first_node)  # Page no.93
        self.head.next = new_node
        # if first_node: # It means first_node is not None
        #     first_node.prev = new_node

    def search(self, item):
        current_node = self.head.next
        while current_node:
            if current_node.data == item:
                return current_node
            current_node = current_node.next
        return None
   
    def remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head.next = node.next
        if node.next:
            node.next.prev = node.prev
            
    def remove(self, item):
        node = self.search(item)
        if node is None:
            return
        self.remove_node(node)

Dll = Doubly_Linked_List()
Dll.append(1)
Dll.append(3)
Dll.append(5)
Dll.append(7)
Dll.append(8)
print(Dll.search(3))
Dll.remove(8)
print(Dll)

# Exercise no.02
  # Cannot Solved // Exercise of Page no.93

# Exercise no.03
  # Cannot Solved // Exercise of Page no.93

# || Exersice of Unit 08 || Recursion ||

# Exercise no.01
def print_number(n):
    if n == 0:
        return
    print(n)
    print_number(n - 1)
if __name__ == "__main__":  # Page no.103
    print_number(5)

# Exercise no.02
def print_number(n):
    if n == 0:
        return
    print_number(n - 1)
    print(n)
if __name__ == "__main__":  # Page no.103
    print_number(5)

# || Exersice of Unit 11 || Heap, Heap Sort & Priority Queue ||

# Exercise no.01
  # Not Codeable // Exercise of Page no.136

# Exercise no.02
    # Cannot Solved // Exercise of Page no.147

# Exercise no.03
    # Cannot Solved // Exercise of Page no.150

# Exercise no.04
    # Cannot Solved // Exercise of Page no.150

# || Exersice of Ending || Last ||

# Exercise no.01
    # Cannot Solved // Exercise of Page no.184

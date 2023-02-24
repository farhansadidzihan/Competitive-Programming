# || =====\\ Linked List is a Dynamic Data Structure (Based on Creating, Linked List is also Static Somewhere) //===== ||

# || Linked List is a series of connected nodes || The elements of linked list is called "Node" || In a linked list, Every node is linked with the next one ||
# || Types of linked list:- Singly linked list, Circular linked list, Doubly linked list ||

# || Singly Linked List ||
class Node:
    ''' An object for storing a single node of singly linked list '''

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)
        # return "<Node data: %s>" % self.data

class Singly_Linked_List:
    ''' It's a Singly linked list '''

    def __init__(self):
        self.head = Node()

    def __repr__(self):
        nodes = []
        current_node = self.head.next
        while current_node: # It means current_node is not None
            nodes.append(repr(current_node))
            current_node = current_node.next
        return "-> ".join(nodes)
    
    def append(self, data):
        node = Node(data)
        if self.head.next is None:
            self.head.next = node
            return # !!!
        current_node = self.head.next
        while current_node.next: # It means current_node.next is not None
            current_node = current_node.next
        current_node.next = node

    def prepend(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def insert(self, data, new_data):
        current_node = self.head.next
        while current_node: # It means current_node is not None
            if current_node.data == data:
                new_node = Node(new_data, current_node.next)
                current_node.next = new_node
                break
            current_node = current_node.next

    def search(self, item):
        current_node = self.head.next
        while current_node: # It means current_node is not None
            if current_node.data == item:
                return current_node
            current_node = current_node.next
        return None

    def remove(self, item):
        previous_node = self.head
        current_node  = previous_node.next
        while current_node: # It means current_node is not None
            if current_node.data == item:
                break
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return None
        if self.head == previous_node:
            self.head.next = current_node.next
        else:
            previous_node = current_node.next

Sll = Singly_Linked_List()
Sll.append(5)
Sll.append(10)
Sll.prepend(1)
Sll.append(50)
Sll.remove(10)
Sll.insert(10, 25)
print(Sll.search(50))
print(Sll)

# || Circular Linked List ||
    # Not Created right now

# || Doubly Linked List ||
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
        new_node = Node(data, None, first_node)
        self.head.next = new_node
        if first_node: # It means first_node is not None
            first_node.prev = new_node

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

# || =====\\ Tree is a Non-Linear Hierarchical Data Structure //===== ||

# || Types of Tree:- Binary Tree, Binary Search Tree, AVL Tree, Heap, B Tree, Segment Tree etc. ||
# || Tree is a Collection of Elements, called "Node" || Each Node contains some value or element in Tree || The Node at the top is called "Root" or origin of the Tree ||
# || In Tree, There can be only one Root Node || Tree Represents the Nodes Connected by Edges || Root does not have a Parent Node ||
# || Parts of Tree:- Root Node, Parent/Ancestor Node, Child/Descendent Node, Leaf/Terminal/External Node, Sibling Node, Edge, Level, Depth, Height || Level Start from 0 to Top-Bottom||

# || 01 || Binary Tree ||
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return repr(self.data)
    
    def add_left(self, node):
        self.left = node
    
    def add_right(self, node):
        self.right = node
    
def create_tree():
    '''  The Tree is :-
           _2_
          /   \
         7     9
        / \      \
       1   6      8
           / \    / \
          5  10  3   4
    '''
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    nine.add_right(eight)
    three = Node(3)
    four = Node(4)
    eight.add_left(three)
    eight.add_right(four)
    return two

print(create_tree())

# || There are Three Algorithms to Traverse a Tree :- Pre Order Traversal, Post Order Traversal, In Order Traversal ||

# || Pre Order Traversal ||
def pre_order(node):
    ''' Post Order Traversl Rule is :-
          _A_
         /   \
        B     C
    '''
    print(node)
    
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)
    
pre_order(create_tree())

# || Post Order Traversal ||
def post_order(node):
    ''' Post Order Traversl Rule is :-
          _C_
         /   \
        A     B
    '''
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node)

post_order(create_tree())

# || In Order Traversal ||
def in_order(node):
    ''' Post Order Traversl Rule is :-
          _B_
         /   \
        A     C
    '''
    if node.left:
        in_order(node.left)
    
    print(node)

    if node.right:
        in_order(node.right)

in_order(create_tree())


# || 02 || Binary Search Tree ||
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
    
    def __repr__(self):
        return repr(self.data)

    def add_left(self, data):
        self.left = node
        if node is not None:
            node.parent = self

    def add_right(self, data):
        self.right = node
        if node is not None:
            node.parent = self

def bst_insert(root, node):
    last_node = None
    current_node = root
    while current_node is not None:
        last_node = current_node
        if node.data < current_node.data:
            current_node = current_node.left
        else:
            current_node = current_node.right
    if last_node is None:
        root = node
    elif node.data < last_node.data:
        last_node.add_left(node)
    else:
        last_node.add_right(node)
    return root

def bst_create():
    root = TreeNode(10)
    for item in [5, 17, 3, 7, 12, 19, 1, 4]:
        node = TreeNode(item)
        root = bst_insert(root, node)
    return root

def in_order(node):
    if node.left:
        in_order(node.left)
    print(node)
    if node.right:
        in_order(node.right)

def bst_search(node, key):
    while node is not None:
        if node.data == key:
            return node
        if key < node.data:
            node = node.left
        else:
            node = node.right
    return node

def bst_minimum(root):
    while root.left is not None:
        root = root.left
    return root

def bst_transplant(root, current_node, new_node):
    if current_node.parent is None:
        root = new_node
    elif current_node == current_node.parent.left:
        current_node.parent.add_left(new_node)
    else:
        current_node.parent.add_right(new_node)
    return root
    
def bst_delete(root, node):
    if node.left is None:
        root = bst_transplant(root, node, node.right)
    elif node.right is None:
        root = bst_transplant(root, node, node.left)
    else:
        min_node = bst_minimum(node.right)
        if min_node.parent != node:
            root = bst_transplant(root, min_node, min_node.right)
            min_node.add_right(node.right)
        root = bst_transplant(root, node, min_node)
        min_node.add_left(node.left)
    return root

if __name__ == "__main__":
    root = bst_create()
    print("BST:-")
    in_order(root)
    for key in [1, 5, 10]:
        node = bst_search(root, key)
        print(f"Will Delete {node}")
        root = bst_delete(root, node)
        print("BST:-")
        in_order(root)

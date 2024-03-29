#This is an implementation of a Binary Search Tree

class Node: #Node class
    def __init__(self, value): #initializing the node
        self.left_child = None
        self.right_child = None
        self.data = value

def insert(root, node): #insertion of each node
    if root is None: #if there is no root, then the inputted node will be the root
        root = node
    else:
        if root.data > node.data: #condition to see if the root is bigger than the node
            if root.left_child is None: #if there is no left child, then the node becomes the left child
                root.left_child = node
            else: #else, go through the function again with the left child of the node
                insert(root.left_child, node)

        else: #same process, except with the right child
            if root.right_child is None:
                root.right_child = node
            else:
                insert(root.right_child, node)

def find(root, node): #finding if a node exists in a tree and prints out True or False
    try:
        if node.data == root.data: #if the node equals the root, then print true
            print(True)

        if node.data < root.data: #if the given node is less than the root, then another condition follows
            if node.data == root.left_child.data: #if node is equal to left child, then print true
                print(True)
            else:
                find(root.left_child, node) #else, then go through the method again with new inputs

        else: #else, go through the right child side with the same implementation as the left child
            if node.data == root.right_child.data:
                print(True)
            else:
                find(root.right_child, node)
    except: #when an error occurs inside the try block, this means that the node does not exist in the tree
        print(False) #therefore, it will print false
#traversals
def in_order(root): #prints out the tree in numerical order
    if not root:
        return
    in_order(root.left_child)
    print(root.data)
    in_order(root.right_child)

def pre_order(root): #prints out the tree starting with the root, then moving to the left child, then the right child
    if not root:
        return
    print(root.data)
    pre_order(root.left_child)
    pre_order(root.right_child)

def post_order(root): #prints out all the nodes from the left child, then the right child, then the root
    if not root:
        return
    post_order(root.left_child)
    post_order(root.right_child)
    print(root.data)



class Node:
    #initializing a node in the node class
    def __init__(self, data):
        self.data = data
        self.next = None

    #LinkedList class
    
class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, newdata): #insertion at the beginning of the linked list
        newNode = Node(newdata)
        self.head = newNode

    def insert_at_end(self, newdata): #insertion at the end of the linked list
        newNode = Node(newdata)
        if self.head is None:
            self.head = newNode
        else:
            last = self.head
            while(last.next):
                last = last.next
            last.next = newNode

    def insert_in_between(self, middle, newdata): #insertion in the middle of the linked list
        if middle is None:
            return
        newNode = Node(newdata)
        newNode.next = middle.next
        middle.next = newNode


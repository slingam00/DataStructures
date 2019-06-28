class Node:
    #initializing a node in the node class
    def __init__(self, data):
        self.data = data
        self.next = None

    #LinkedList class
    
class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data): #insertion at the beginning of the linked list
        newNode = Node(data)
        self.head = newNode

    def insert_at_end(self, data): #insertion at the end of the linked list
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            last = self.head
            while(last.next):
                last = last.next
            last.next = newNode

    def insert_in_between(self, middle, data): #insertion in the middle of the linked list
        if middle is None:
            return
        newNode = Node(data)
        newNode.next = middle.next
        middle.next = newNode

    def remove_first_node(self, data):
        if self.data is self.head:
            self.head = self.head.next

    def remove_last_node(self, data):
        if self.data.next is None:
            self.data = None

    def remove_in_between(self, data):
        if Node.next == self.data:
            Node.next = self.data.next
            self.data = None


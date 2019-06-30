# This is a queue implementation using lists

class Queue: #
    def __init__(self): #initializing the queue with an empty list
        self.queue = []

    def enqueue(self, item): #as the enqueue method is called, the list is being appended
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0: #if there is nothing in the queue, then the method returns a message
            return "The queue is empty"

        self.queue.remove(self.queue[0]) #otherwise, remove the first element of the queue

    def size(self): #displaying the size of the queue
        return len(self.queue)

    def show(self): #displaying the queue itself
        return self.queue


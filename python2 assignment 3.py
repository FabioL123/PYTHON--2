class Queue:
    def __init__(self):
        self.items = []

    # Add an item to the end of the queue
    def enqueue(self, item):
        self.items.append(item)

    # Remove and return the item at the front of the queue
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)

    # Check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # Return the number of items in the queue
    def size(self):
        return len(self.items)
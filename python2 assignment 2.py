# Node class represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Remove the first occurrence of data
    def remove(self, data):
        # If list is empty
        if self.head is None:
            print("List is empty")
            return

        # If the head node contains the data
        if self.head.data == data:
            self.head = self.head.next
            return

        # Traverse the list
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

        print("Value not found in the list")

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
# Node class represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Add a node to the end of the list
    def append(self, data):
        new_node = Node(data)

        # If the list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # Add a node to the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Print all elements in the list
    def print_list(self):
        current = self.head

        if current is None:
            print("The list is empty")
            return

        while current:
            print(current.data)
            current = current.next
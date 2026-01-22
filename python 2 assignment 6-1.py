class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    # Base case: empty list or single node
    if head is None or head.next is None:
        return head

    # Reverse the rest of the list
    new_head = reverse_linked_list(head.next)

    # Fix the links
    head.next.next = head
    head.next = None

    return new_head


# ----- Create your own list -----
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

# Reverse the list
head = reverse_linked_list(head)

# Print reversed list
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
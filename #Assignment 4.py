#Assignment 4

class Node:
    # Node class to store data and reference to the next node.
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # LinkedList class to manage a collection of nodes
    def __init__(self):
        self.head = None  # Initializes an empty list with no head node.

    # Adds a new value to the end of the linked list
    def add(self, value):
        new_node = Node(value)
        if not self.head:  # If list is empty, it sets a new node as the head.
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverses to the last node.
                current = current.next
            current.next = new_node  # Links last node to the new node.

    # Removes the element at a specified index.
    def remove(self, index):
        if self.head is None:  # Checks if list is empty.
            raise IndexError("List is empty")
        
        if index == 0:  # If removing the head node.
            self.head = self.head.next  # Moves head to the next node
            return
        
        # Traverses to the node before the one to remove.
        current = self.head
        prev = None
        for i in range(index):
            prev = current
            current = current.next
            if current is None:
                raise IndexError("Index out of range")
        
        prev.next = current.next  # Bypasses the node to remove it.

    # Retrieves the value at a specified index.
    def get(self, index):
        current = self.head
        for _ in range(index):
            if current is None:  # Index is out of range.
                raise IndexError("Index out of range")
            current = current.next
        if current is None:  # Finalizes check for out of range.
            raise IndexError("Index out of range")
        return current.value  # Returns the value at the specified index.

    # Checks if the linked list is empty.
    def is_empty(self):
        return self.head is None

    # Returns the value of the first element in the list
    def first(self):
        return self.head.value if self.head else None  # Returns None if list is empty

    # Returns the value of the last element in the list.
    def last(self):
        if not self.head:
            return None  # Returns None if list is empty
        current = self.head
        while current.next:  # Traverses to the last node
            current = current.next
        return current.value

    # Reverses the order of nodes in the linked list.
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Temporarily stores the next node.
            current.next = prev  # Reverses the current node's next pointer.
            prev = current  # Moves previous and current one step forward.
            current = next_node
        self.head = prev  # Sets the head to the new first node after reversing.

# Main function 
def main():
    linked_list = LinkedList()  # Creates a new LinkedList object.
    linked_list.add(1)  # Adds elements to the list.
    linked_list.add(2)
    linked_list.add(3)
    
    print("First element:", linked_list.first())  # Outputs the first element (should be 1)
    print("Last element:", linked_list.last())  # Outputs the last element (should be 3)
    print("Is empty?", linked_list.is_empty())  # Checks if the list is empty (should be False)
    
    linked_list.reverse()  # Reverses the linked list.
    print("First element after reversing:", linked_list.first())  # Output the first element after reversing (should be 3)
    
    linked_list.remove(1)  # Removes element at index 1.
    print("Element at index 1 after removal:", linked_list.get(1))  # Output element at index 1 after removal (should be 1)

# calls the main function.
main()


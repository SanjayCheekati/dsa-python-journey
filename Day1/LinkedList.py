class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        
    def insert_at_pos(self, val, pos):
        if pos == 1:
            return self.insert_at_beginning(val)
        new_node = Node(val)
        curr = self.head
        for _ in range(pos - 2):
            if not curr:
                print("Out of bounds")
                return
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        
    def update_by_value(self, old_val, new_val):
        curr = self.head
        while curr:
            if curr.val == old_val:
                curr.val = new_val
                print("Value updated!")
                self.display()
                return
            curr = curr.next
            
    def update_by_pos(self, pos, new_val):
        curr = self.head
        i = 1
        while curr:
            if i == pos:
                curr.val = new_val
                print("Value updated!!")
                self.display()
                return
            curr = curr.next
            i += 1
        print("Invalid position")
        
    def search(self, val):
        curr = self.head
        i = 1
        while curr:
            if curr.val == val:
                print("Found at position:",i, end= " ")
                return True
            curr = curr.next
            i += 1
        return "Not Found"
        
    def display(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print(' -> '.join(elements) if elements else "Empty List")

ll = LinkedList()
ll.insert_at_beginning(1)
ll.insert_at_end(8)
ll.insert_at_pos(3, 1)
ll.insert_at_pos(6, 2)
ll.display()
print(ll.search(7))
ll.update_by_value(1, 9)
ll.update_by_pos(2, 4)
            
# NODE AT A GIVEN POSITION IN LINKED LIST

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def insert_after_node(self, node, data):
        if not node:
            return
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    def delete_node(self, key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        prev_node = None
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next
        if not curr_node:
            return
        prev_node.next = curr_node.next
        curr_node = None

    def delete_node_at_pos(self, pos):
        curr_node = self.head
        if pos == 0:
            self.head = curr_node.next
            curr_node = None
            return
        prev_node = None
        count = 0
        while curr_node and count != pos:
            prev_node = curr_node
            curr_node = curr_node.next
            count += 1
        if not curr_node:
            return
        prev_node.next = curr_node.next
        curr_node = None

    def node_at_pos(self,pos):
        count = 1
        temp = self.head
        while temp is not None:
            if count == pos:
                print(f"The value at {pos} node is {temp.data}")
            temp = temp.next
            count = count + 1
        return
        
    def search(self, key):
        curr_node = self.head
        while curr_node:
            if curr_node.data == key:
                return True
            curr_node = curr_node.next
        return False

    def get_length(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()
        
ll = LinkedList()
ll.insert_at_end(5)
ll.insert_at_end(10)
ll.insert_at_end(15)
ll.insert_at_end(20)

ll.node_at_pos(2)
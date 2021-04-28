from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        temporary_node = self.head

        while temporary_node.next is not None:
            temporary_node = temporary_node.next

        temporary_node.next = node

    def prepend_node(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def display(self, x):
        elems = []
        cur_node = self.head
        if cur_node == x:
            print("contains ")
        while cur_node.next is not None:
            if cur_node.data == x:
                print("contains ")
            cur_node = cur_node.next
            elems.append(cur_node.data)
        if cur_node.next is None:
            if cur_node.data == x:
                print('contains')

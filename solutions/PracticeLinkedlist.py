"""To practice linked list details """


class Node:
    """ The purpose of this class is to have a Node functionality  
    """
    def __init__(self):
        self.val = None
        self.next = None

class LinkedList:
    """To have LinkedList functionality"""

    def __init__(self):
        self.head = None

    def traverse(self):
        if not self.head:
            return "Empty list"
        temp = self.head
        while temp :
            print(temp.val,",")

            temp = temp.next

    def insert_at_start(self,data):
        node = Node()
        node.val = data
        node.next = self.head
        self.head = node 
        
    def inser_at_end(self,data):
        node = Node()
        node.val = data
        temp = self.head 
                while not temp:
            temp = temp.next
        temp.nexti = node

l1 = LinkedList()
l1.traverse()
l1.insert_at_start(5)
l1.insert_at_start(4)
l1.traverse()   


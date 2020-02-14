## INsertion at begining
 
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=' ')
            tmp = tmp.next
        print('\n')

    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head=newNode

    def remove(self, key):
        pass


l = LinkedList()
l.head = Node(2)
n2 = Node(3)
n3 = Node(4)
n4 = Node('Debjit')
l.head.next = n2
n2.next = n3
n3.next=n4
l.printList()
l.insertAtBeginning(-100)
l.printList()
l.remove(3)
l.printList()
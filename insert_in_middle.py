## Insert in the middle  of a linked list
 
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

    def insertAtMiddle(self, insertData, data):
        newNode = Node(data)
        tmp = self.head
        while tmp:
            if tmp.data == insertData:
                break
            else:
                tmp = tmp.next
        newNode.next = tmp.next
        tmp.next = newNode
        

l = LinkedList()
l.head = Node(2)
n2 = Node(3)
n3 = Node(4)
n4 = Node('Debjit')
l.head.next = n2
n2.next = n3
n3.next=n4
print('Before Insertion')
l.printList()
l.insertAtMiddle(2, 50)
print('After insertion')
l.printList()
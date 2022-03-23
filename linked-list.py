class Node:
    def __init__(self, data):
        # assign the value
        self.data = data
        # initialize next as null
        self.next = None

# Linked List class with some methods to check if it works
class LinkedList:
    def __init__(self):
        self.head = None

    # define a method that prints all elems in linked list
    def printNodes(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    # define a method that adds new item to end of list
    def addLast(self, data):
        tempNode = Node(data)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = tempNode
        else:
            self.head = tempNode

    # define a method that adds new item to beginning of list
    def addFirst(self, data):
        tempNode = Node(data)
        if self.head:
            tempNode2 = self.head
            self.head = tempNode
            tempNode.next = tempNode2
        else:
            self.head = tempNode




llist = LinkedList()
llist.addLast(1)
llist.addLast(2)
llist.addLast(3)
llist.addLast(4)
llist.printNodes()



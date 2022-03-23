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

    # define a method that removes the first item of list
    def removeFirst(self):
        tempNode = self.head.next
        self.head = tempNode

    # define a method that removes the last item of list
    def removeLast(self):
        if self.head:
            if self.head.next:
                curr = self.head
                while curr.next.next:
                    curr = curr.next
                curr.next = None
            else:
                self.head = None

    # define a method that gets the size of the linked list
    def size(self):
        if self.head:
            counter = 0
            curr = self.head
            while (curr):
                curr = curr.next
                counter += 1
            return counter
        else:
            return 0

    # define a method that returns true if an item exists in linked list
    def exists(self, value):
        if self.head:
            curr = self.head
            while (curr):
                if curr.data == value:
                    return True
                curr = curr.next
            return False
        return False




llist = LinkedList()
llist.addLast(1)
llist.addLast(2)
llist.addLast(3)
llist.addLast(4)
llist.removeLast()
llist.removeLast()
llist.removeLast()
llist.addLast(2)
llist.addLast(3)
llist.addLast(4)
print(llist.size())
print(llist.exists(1))
print(llist.exists(5))
llist.printNodes()



class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self) :
        self.head = None

    def push(self,data) :
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def printList(self) :
        temp = self.head
        while(temp) :
            print(temp.data,end = ' ')
            temp = temp.next

    def getNthfromLast(self,n) :
        length = 0
        temp = self.head
        while(temp) :
            temp = temp.next
            length = length + 1
        if n > length :
            print('out of list')
        temp = self.head
        for i in range(length-n) :
            temp = temp.next
        print(temp.data)

llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(1)
llist.push(9)
llist.push(7)
llist.push(6)
llist.printList()
print('\n')
llist.getNthfromLast(7)

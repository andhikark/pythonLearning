class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while current_node != None and position + 1 != index:
                position += 1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not found")

    def remove_first(self):
        if self.head is None:
            return
        self.head = self.head.next

    def remove_last(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def remove_at_index(self, index):
        if self.head is None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first()
        else:
            while current_node != None and position + 1 != index:
                position += 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not found")

    def remove_by_value(self,value):
        current_node = self.head
        if current_node.data == value:
            self.remove_first()
            return

        while(current_node != None and current_node.next.data != value):
            current_node = current_node.next

        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next

    def sizeOfLL(self):
        count = 0
        if self.head:
            current_node = self.head
            while(current_node):
                count += 1
                current_node = current_node.next
            return count
        else:
            return 0

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" --> ")
            current_node = current_node.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtBegin(2)
    ll.insertAtBegin(1)
    ll.insertAtEnd(3)
    ll.insertAtBegin(22)
    ll.insertAtIndex(23,2)
    ll.printLL()
    print()
    ll.insertAtIndex(4, 2)
    ll.remove_first()
    ll.remove_last()
    ll.remove_at_index(2)
    ll.printLL()
    ll.insertAtBegin(12)
    ll.insertAtEnd(100)
    print()
    ll.printLL()
    ll.remove_by_value(100)
    print()
    ll.printLL()
    print()
    print("the size of the linked list is " + str(ll.sizeOfLL()))


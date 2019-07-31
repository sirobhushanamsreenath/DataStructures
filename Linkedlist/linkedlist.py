class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None


class LinkedList():

    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, data):
        new_node = Node()
        new_node.data = data
        # print(self.length)
        if self.length == 0:
            self.head = new_node
            self.length += 1
        else:
            current = self.head
            while current.has_next():
                current = current.get_next()
            current.set_next(new_node)
            self.length += 1

    def find_nth_element(self, n):
        count = 0
        current = self.head
        while current:
            count += 1
            if count == n:
                print('The element at position {} is {}'.format(n, current.data))
            else:
                current = current.get_next()

    def printNode(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.get_next()

    def find_middle_element(self):
        count = 0
        mid_pos = int(self.length / 2)
        if self.length == 0:
            print('list is empty. So no middle element')
            return
        if self.length % 2 == 0:
            print('mid elements are at position {} and {}'.format(
                int(mid_pos), int(mid_pos + 1)))
            current = self.head
            while current:
                count += 1
                if mid_pos == count or mid_pos + 1 == count:
                    print('element at position {} is {}'.format(
                        mid_pos, current.data))
                current = current.get_next()
        else:
            print('mid element is at position {}'.format(mid_pos))
            current = self.head
            while current:
                # count += 1
                if mid_pos == count:
                    print('element at position {} is {}'.format(
                        mid_pos, current.data))
                current = current.get_next()
                count += 1


mylist = LinkedList()
print('inserting in linked list')
mylist.insert(1)
mylist.insert(2)
mylist.insert(3)
mylist.insert(8)
mylist.insert(10)
mylist.insert(11)
mylist.insert(12)
mylist.insert(13)
mylist.insert(14)
mylist.insert(15)
print('Elements of linked list')
mylist.printNode()
mylist.find_nth_element(3)
mylist.find_middle_element()

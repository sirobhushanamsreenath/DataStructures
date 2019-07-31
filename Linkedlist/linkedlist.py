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
            new_node.set_next(self.head)
            self.head = new_node
            self.length += 1
        return True

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
            print(current.data)
            current = current.get_next()

    def find_middle_element(self):
        count = 0
        mid_pos = self.length / 2
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
                count += 1
                if mid_pos == count:
                    print('element at position {} is {}'.format(
                        mid_pos, current.data))
                current = current.get_next()


mylist = LinkedList()
print('inserting in linked list')
print(mylist.insert(1))
print(mylist.insert(2))
print(mylist.insert(3))
print(mylist.insert(8))
print(mylist.insert(10))
print(mylist.insert(11))
print(mylist.insert(12))
print(mylist.insert(13))
print(mylist.insert(14))
print(mylist.insert(15))
print('Elements of linked list')
mylist.printNode()
# mylist.find_nth_element(3)
mylist.find_middle_element()

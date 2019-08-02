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

    # The below function will add the elements at last in the linked list.
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
        print('Elements in the linked list')
        while current:
            print(current.data)
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

    def insert_at_beginning(self, data):
        new_node = Node()
        new_node.set_data(data)
        if self.length == 0:
            self.head = new_node
            self.length += 1
        else:
            current = self.head
            new_node.set_next(current)
            self.head = new_node
            self.length += 1

    def insert_at_middle(self, pos, data):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insert_at_beginning(data)
            else:
                current = self.head
                new_node = Node()
                new_node.set_data(data)
                count = 0
                while count < pos - 1:
                    count += 1
                    current = current.get_next()
                new_node.set_next(current.get_next())
                current.set_next(new_node)
                self.length += 1

    def insert_at_end(self, data):
        current = self.head
        new_node = Node()
        new_node.set_data(data)
        while current.has_next():
            current = current.get_next()
        current.set_next(new_node)
        new_node.set_next(None)
        self.length += 1

    def delete_at_beginning(self):
        if self.length == 0:
            print('List is empty')
        else:
            current = self.head
            self.head = current.get_next()
            current.set_next(None)
            self.length -= 1

    def delete_at_middle(self, data):
        current = self.head
        previous = self.head
        while current:
            if current.data == data:
                previous.set_next(current.get_next())
                current.set_next(None)
                self.length -= 1
                return
            previous = current
            current = current.get_next()

    def delete_at_end(self):
        current = self.head
        previous = current
        while current.has_next():
            previous = current
            current = current.get_next()
        previous.set_next(None)
        self.length -= 1


mylist = LinkedList()
mylist.insert(2)
mylist.insert(3)
mylist.insert(5)
mylist.printNode()
mylist.insert_at_beginning(1)
mylist.insert_at_middle(3, 4)
mylist.insert_at_end(6)
mylist.delete_at_beginning()
mylist.delete_at_middle(4)
mylist.delete_at_end()
mylist.printNode()

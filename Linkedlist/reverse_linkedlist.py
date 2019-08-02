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


class LinkeList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_begin(self, data):
        new_node = Node()
        new_node.set_data(data)
        if self.length == 0:
            self.head = new_node
            self.length += 1
        else:
            current = self.head
            new_node.set_next(current)
            # new_node = self.head
            self.head = new_node
            self.length += 1

    def insert_at_middle(self, pos, data):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insert_at_begin(data)
            else:
                count = 0
                new_node = Node()
                new_node.set_data(data)
                current = self.head
                while count < pos - 1:
                    count += 1
                    current = current.get_next()
                new_node.set_next(current.get_next())
                current.set_next(new_node)
                self.length += 1

    def insert_at_end(self, data):
        if self.length == 0:
            self.insert_at_begin(data)
        else:
            current = self.head
            new_node = Node()
            new_node.set_data(data)
            while current.has_next():
                current = current.get_next()
            current.set_next(new_node)
            new_node.set_next(None)
            self.length += 1

    def printNode(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()

    def reverse_linkedlist(self):
        previous = None
        current = self.head
        while current:
            # print(current.get_data())
            nextnode = current.get_next()
            current.set_next(previous)
            previous = current
            current = nextnode
        self.head = previous


mylist = LinkeList()
mylist.insert_at_end(1)
mylist.insert_at_end(2)
mylist.insert_at_end(3)
mylist.insert_at_end(4)
mylist.insert_at_end(5)
mylist.insert_at_end(6)
mylist.printNode()
mylist.reverse_linkedlist()
print('reversed linked list')
mylist.printNode()

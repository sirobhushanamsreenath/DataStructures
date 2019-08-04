
class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def set_previous(self, previous):
        self.previous = previous

    def get_previous(self):
        return self.previous

    def has_next(self):
        return self.next != None

    def has_previous(self):
        return self.previous != None


class DoubleLinkedList:
    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.length = 0

    def insert_at_beginning(self, data):
        new_node = Node(data, None, None)
        if self.tail == None:
            self.head = self.tail = new_node
            self.length += 1
        else:
            current = self.head
            new_node.set_next(current)
            current.set_previous(new_node)
            self.head = new_node
            self.length += 1
        # import ipdb
        # ipdb.set_trace()

    def insert_at_ending(self, data):
        if self.length == 0 and self.head == self.tail:
            self.insert_at_beginning(data)
        else:
            new_node = Node(data, None, self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node
            self.length += 1

    def insert_at_middle(self, pos, data):
        # need to change
        # if pos > self.length or pos < 0:
        #     return None
        # else:
        if pos <= 0:
            self.insert_at_beginning(data)
        # need to change
        elif pos >= self.length:
            self.insert_at_ending(data)
        else:
            current = self.head
            count = 0
            while (count < pos-1):
                current = current.get_next()
                count += 1
            new_node = Node(data, current.get_next(), current)
            # new_node.set_next(current.get_next())
            # new_node.set_previous(current)
            current.get_next().set_previous(new_node)
            current.set_next(new_node)
            self.length += 1

    def delete_at_beginning(self):
        if self.length == 0:
            print('List is empty')
        else:
            current = self.head
            temp = self.head
            self.head = current.get_next()
            temp.set_previous(None)
            self.length -= 1

    def delete_at_ending(self):
        current = self.head
        while current.has_next():
            current = current.get_next()
        current.get_previous().set_next(None)
        current.set_next(None)
        self.length -= 1

    def delete_at_middle(self, pos):
        if pos > self.length or pos < 0:
            return None
        else:
            # This will delete nodes, irrespective of data
            if pos == 0:
                self.delete_at_beginning()
            elif pos >= self.length - 1:
                self.delete_at_ending()
            else:
                count = 0
                current = self.head
                while count < pos - 1:
                    current = current.get_next()
                    count += 1
                current.set_next(current.get_next().get_next())
                current.get_next().set_previous(current)
                self.length -= 1

    def print_linked_list(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()


mylist = DoubleLinkedList()
# mylist.insert_at_beginning(2)

# mylist.insert_at_ending(3)
# mylist.insert_at_ending(4)
mylist.insert_at_beginning(1)
mylist.insert_at_ending(3)
# mylist.print_linked_list()
mylist.insert_at_middle(1, 2)
mylist.delete_at_beginning()
# mylist.delete_at_beginning()
# mylist.delete_at_beginning()
# mylist.print_linked_list()
# mylist.delete_at_beginning()
# mylist.print_linked_list()
mylist.delete_at_ending()
# mylist.print_linked_list()
# mylist.delete_at_middle(10)
print('After insertion')
mylist.print_linked_list()

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
        if self.length == 0 and self.head == self.tail:
            self.head = self.tail = new_node
            self.length += 1
        else:
            current = self.head
            new_node.set_next(current)
            current.set_previous(new_node)
            self.head = new_node
            self.length += 1

    def insert_at_ending(self, data):
        if self.length == 0 and self.head == self.tail:
            self.insert_at_beginning(data)
        else:
            current = self.head
            while current.has_next():
                current = current.get_next()
            current.set_next(Node(data, None, current))
            self.tail = current.get_next()
            self.length += 1

    def insert_at_middle(self, pos, data):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insert_at_beginning(data)
            else:
                current = self.head
                # print(current.get_data())
                new_node = Node(data, None, None)
                # print(new_node.get_data())
                count = 0
                # print(pos)
                while (count < pos-1):
                    # print(pos)
                    current = current.get_next()
                    count += 1
                new_node.set_next(current.get_next())
                # print(new_node.get_next().get_data())
                new_node.set_previous(current)
                # print(new_node.get_previous().get_data())
                temp = current.get_next()
                temp.set_previous(new_node)
                # print(current.get_next().get_previous().get_data())
                new_node.set_previous(current)
                # print(new_node.get_previous().get_data())
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

    # Under development

    # def delete_at_ending(self):
    #     current = self.head
    #     # print(current)
    #     while current.has_next():
    #         print('current is : {}', current.get_data())
    #         current = current.get_next()
    #     # current.set_next(None)
    #     # print(current.get_data())
    #     current.set_previous(None)
    #     current.get_previous().set_next(None)
    #     self.length -= 1

    def print_linked_list(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()


mylist = DoubleLinkedList()
mylist.insert_at_beginning(1)
mylist.insert_at_beginning(2)
mylist.insert_at_ending(3)
# mylist.insert_at_middle(2, 4)
# mylist.delete_at_beginning()
# mylist.delete_at_beginning()
# mylist.delete_at_beginning()
# mylist.print_linked_list()
# mylist.delete_at_beginning()
# mylist.print_linked_list()
mylist.delete_at_ending()
mylist.print_linked_list()

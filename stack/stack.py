class Node:
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data

    def has_next(self):
        return self.next != None


class Stack:
    def __init__(self, top=None):
        self.top = top

    def print_stack(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next

    def push(self, data):
        current = self.top
        if self.top == None:
            new_node = Node(data, None)
            self.top = new_node
        else:
            new_node = Node(data, current)
            self.top = new_node

    def pop(self):
        current = self.top
        if self.top == None:
            print('The stack is empty')
        else:
            self.top = current.next


mystack = Stack()
mystack.push(2)
mystack.push(1)
mystack.pop()
mystack.print_stack()

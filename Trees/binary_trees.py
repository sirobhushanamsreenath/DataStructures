class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


class BinaryTree():
    def __init__(self, root=None):
        self.root = root
        self.length = 0

    def insert_root(self, data):
        new_node = BinaryTreeNode(data, None, None)
        self.root = new_node

    def insert_left(self, data):
        current = self.root
        new_node = BinaryTreeNode(data, None, None)
        while current.left:
            current = current.left
        current.left = new_node

    def insert_right(self, data):
        current = self.root
        new_node = BinaryTreeNode(data, None, None)
        while current.right:
            current = current.right
        current.right = new_node

    def print_tree_preorder(self, root):
        current = root
        if not current:
            return
        elif root:
            self.print_tree_preorder(current.get_left())
            print(current.get_data())
            self.print_tree_preorder(current.get_right())


mytree = BinaryTree()
mytree.insert_root('A')
mytree.insert_left('B')
mytree.insert_right('C')
mytree.print_tree_preorder(mytree)

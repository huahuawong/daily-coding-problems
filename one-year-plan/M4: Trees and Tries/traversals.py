# https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
# https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left_child is None:
                    self.left_child = BinaryTree(data)
                else:
                    self.left_child.insert(data)
            elif data > self.data:
                if self.right_child is None:
                    self.right_child = BinaryTree(data)
                else:
                    self.right_child.insert(data)
        else:
            self.data = data

    # Print the Tree
    def PrintTree(self):
        if self.left_child:
            self.left_child.PrintTree()
        print( self.data),
        if self.right_child:
            self.right_child.PrintTree()

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()

        print(self.data)

        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()

        if self.right_child:
            self.right_child.post_order()

        print(self.data)


root = BinaryTree(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
# root.PrintTree()
# root.in_order()
root.post_order()
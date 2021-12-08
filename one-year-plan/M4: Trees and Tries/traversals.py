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

    # Print the Tree, this is actually post-order traversal printing
    def print_tree(self):
        if self.left_child:
            self.left_child.print_tree()
        if self.right_child:
            self.right_child.print_tree()
        print(self.data)

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()

        print(self.data)

        if self.right_child:
            self.right_child.in_order()

    def pre_order(self):
        print(self.data)

        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.pre_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()

        if self.right_child:
            self.right_child.post_order()

        print(self.data)


def height(root):
    # Check if the binary tree is empty
    if root is None:
        return 0
    # Recursively call height of each node
    leftAns = height(root.left_child)
    rightAns = height(root.right_child)

    # Return max(leftHeight, rightHeight) at each iteration
    return max(leftAns, rightAns) + 1


def level_order_traversal(root):
    h = height(root)
    for i in range(1, h+1):
        printcurrentHeight(i, root)


def printcurrentHeight(height, root):
    if height == 1:
        print(root.data)
    if root is None:
        return
    printcurrentHeight(height-1, root.left_child)
    printcurrentHeight(height-1, root.right_child)


# Vertical traversal
def findMinMax(root, min, max, h_dist):
    if root is None:
        return
    if h_dist < min[0]:
        min[0] = h_dist
    elif h_dist > max[0]:
        max[0] = h_dist
    findMinMax(root.left_child, min, max, h_dist-1)
    findMinMax(root.right_child, min, max, h_dist+1)
    # print(max); print(min)


def printVerticalLine(root, line_num, h_dist):
    if root is None:
        return
    if h_dist == line_num:
        print(root.data)
    printVerticalLine(root.left_child, line_num, h_dist-1)
    printVerticalLine(root.right_child, line_num, h_dist+1)


def verticalOrder(root):
    # Find min and max distances with respect to root
    minimum = [0]
    maximum = [0]
    findMinMax(root, minimum, maximum, 0)
    # print("Min is: ", minimum[0]); print("Max is: ", maximum[0])

    # Iterate through all possible lines starting from the leftmost line and print nodes line by line
    for line_no in range(minimum[0], maximum[0] + 1):
        print("At line number ", line_no)
        val = printVerticalLine(root, line_no, 0)
        if val is not None:
            print(val)
        # print(printVerticalLine(root, line_no, 0))


root = BinaryTree(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.insert(40)
root.insert(45)


# root.print_tree()
# root.in_order()
# root.pre_order()
# root.post_order()
print("Height of the binary tree is: " + str(height(root)))

# level_order_traversal(root)
# findMinMax(root, 0, 0, 0)

# vertical order traversal
print("Vertical order traversal is: \n")
verticalOrder(root)

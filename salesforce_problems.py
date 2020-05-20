# Q1 This problem was asked by Salesforce.
# Write a program to merge two binary trees. Each node in the new tree should hold a value equal to the sum of the
# values of the corresponding nodes of the input trees.
# If only one input tree has a node in a given position, the corresponding node in the new tree should match that
# input node.

class Node:
    def __init__(self, val):
        self.val = val
        self.l = self.r = None


# In order traversal of the binary tree, we can always do preorder or postorder
def inorder(node):
    # if the value is empty at node
    if not node:
        return

    # recursively in order traversal from left to right
    inorder(node.l)
    print(node.val, end=" ")
    inorder(node.r)


def merge(t1, t2):
    if not t1:
        return t2
    if not t2:
        return t1

    # recursively summing up the binary tree values together
    t1.val += t2.val
    t1.l = merge(t1.l, t2.l)
    t1.r = merge(t1.r, t2.r)

    # return t1 that has been modified to sum up the 2 binary trees, alternatively we can use t3 to differentiate
    return t1


# Drive code
root_1 = Node(1)
root_1.l = Node(2)
root_1.r = Node(3)
root_1.l.l = Node(4)

root_2 = Node(2)
root_2.l = Node(2)
root_2.r = Node(3)

final_root = merge(root_1, root_2)
print("The Merged Binary Tree is:")
inorder(final_root)
assert final_root.val == 3

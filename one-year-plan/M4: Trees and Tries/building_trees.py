# 1. Building trees from using inorder and preorder traversals
# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# def buildTree(in_ord, pre_ord, in_start, in_end):
#     if in_start > in_end:
#         return None
#
#     t_node = Node(pre_ord[buildTree.preIndex])
#     print("Data at node: ", t_node.data)
#     buildTree.preIndex += 1
#     print("Pre-index: ", buildTree.preIndex)
#     print("In start: ", in_start)
#     print("In end: ", in_end)
#
#     # If this node has no children then return
#     if in_start == in_end:
#         return t_node
#
#     # Else find the index of this node in Inorder traversal
#     inIndex = search(in_ord, in_start, in_end, t_node.data)
#     print("In-order index: ", inIndex)
#
#     # Using index in Inorder Traversal, construct left
#     # and right subtrees
#     t_node.left = buildTree(in_ord, pre_ord, in_start, inIndex - 1)
#     t_node.right = buildTree(in_ord, pre_ord, inIndex + 1, in_end)
#     return t_node
#
#
# # This function is to search for the index of the root node in the in_order array. The 'value' here refers to the
# # the first value in the pre_order array, as the first value indicates the root node
def search(arr, start, end, value):
    for i in range(start, end+1):
        if arr[i] == value:
            return i


# to test if the tree built is in order
def print_inorder(node):
    if node is None:
        return
    print_inorder(node.left)
    print(node.data)
    print_inorder(node.right)


# # to test if the tree built is in order
def print_preorder(node):
    if node is None:
        return

    print(node.data)
    print_preorder(node.left)
    print_preorder(node.right)
#
#
# # Driver program to test above function
# inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
# preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
#
# # Static variable preIndex
# buildTree.preIndex = 0
# root = buildTree(inOrder, preOrder, 0, len(inOrder) - 1)
#
# # Let us test the build tree by printing Inorder traversal
# print("Inorder traversal of the constructed tree is: ")
# print_inorder(root)
#
# print("Pre-order traversal of the constructed tree is: ")
# print_preorder(root)


# 2. Building trees from using inorder and postorder traversals
def buildUtil(In, post, inStrt, inEnd, pIndex):
    # Base case
    if inStrt > inEnd:
        return None

    # Pick current node from Postorder traversal using postIndex and decrement postIndex
    node = Node(post[pIndex[0]])
    pIndex[0] -= 1

    # If this node has no children then return
    if inStrt == inEnd:
        return node

    # Else find the index of this node in Inorder traversal
    iIndex = search(In, inStrt, inEnd, node.data)

    # Using index in Inorder traversal, construct left and right subtress
    node.left = buildUtil(In, post, inStrt, iIndex - 1, pIndex)
    node.right = buildUtil(In, post, iIndex + 1, inEnd, pIndex)
    return node


def print_postorder(root):
    if root is None:
        return
    print_postorder(root.left)
    print_postorder(root.right)
    print(root.data)


# Driver program to test above function
inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
postOrder = ['D', 'E', 'B', 'F', 'C', 'A']

# Static variable preIndex
pIndex = [len(inOrder) - 1]
root = buildUtil(inOrder, postOrder, 0, len(inOrder) - 1, pIndex)

# Let us test the build tree by printing Inorder traversal
print("Inorder traversal of the constructed tree is: ")
print_inorder(root)

print("Post-order traversal of the constructed tree is: ")
print_postorder(root)

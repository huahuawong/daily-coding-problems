# This problem was asked by Google.

# Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

# One way is to find the height of the tree before finding the root data that is at that height

def height(root):
  if not root:
    return None
  left_depth = height(root.left_child)
  right_depth = height(root.right_child)
  return max(left_depth, right_depth) + 1 



def deepestNode(root, levels):
    if not root:
        return
    if levels == 1:
        print(root.data)
    # if the height is not 1, keep iterating until we print the deepest node (i.e. when levels = 1)
    elif levels > 1:
        deepestNode(root.left_child, levels - 1)
        deepestNode(root.right_child, levels - 1)


levels = height(root)
deepestNode(root, levels)

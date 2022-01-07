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



# This problem was asked by Yext.
# Two nodes in a binary tree can be called cousins if they are on the same level of the tree but have different parents. For example, in the following diagram 4 and 6 are cousins
def findlevel(root, target, index=1, level=0):
  if root is None or level != 0:
    return 0
  if root == target:
    level = index
  level = findlevel(root.left, target, index+1, level)
  level = findlevel(root.right, target, index+1, level)
  return level

def printLevel(root, target, level):
  # base case
  if root is None:
      return

  # print cousins
  if level == 1:
      print(root.key, end=' ')
      return
  
  # recur for the left and right subtree if the given node
  # is not a child of the root
  if (not (root.left is not None and root.left == node or
           root.right is not None and root.right == node)):
      printLevel(root.left, node, level - 1)
      printLevel(root.right, node, level - 1)
      
# Function to print all cousins of a given node
def printAllCousins(root, node):
  # base case
  if not root or root == node:
      return

  # find the level of the given node
  level = findLevel(root, node)
  print("Found level:", level)

  # print all cousins of the given node using its level number
  printLevel(root, node, level)







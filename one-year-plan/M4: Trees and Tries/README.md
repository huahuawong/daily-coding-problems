### Trees and Tries

1. Different components of a tree (Node, root, subtree etc)

A tree is a collection of entities called nodes. Nodes are connected by edges. Each node contains a value or data, and it may or may not have a child node.
Root node referes to either the topmost or the bottom node in a tree data structure, depending on how the tree is represented visually.

Creating a Root:

```
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      print(self.data)

root = Node(10)
root.PrintTree()
```

2. Binary tree and N-ary tree
A binary tree is a tree data structure in which each node has at the most two children, which are referred to as the left child and the right child
If a tree is a rooted tree in which each node has no more than N children, it is called N-ary tree. Trie is a N-ary tree where N = 3.

3. Balanced tree
A balanced binary tree, also referred to as a height-balanced binary tree, is defined as a binary tree in which the height of the left and right subtree of any node differ by not more than 1

4. Binary Search Tree
BST has the following requirements:

* The left subtree of a node contains only nodes with keys lesser than the node’s key.
* The right subtree of a node contains only nodes with keys greater than the node’s key.
* The left and right subtree each must also be a binary search tree.

5. Complete vs Full vs Perfect Tree
* Complete Binary Tree: A Binary Tree is complete Binary Tree if all levels are completely filled except possibly the last level and the last level has all keys as left as possible.
* Full Binary Tree: A Binary Tree is full if every node has 0 or 2 children. Following are examples of a full binary tree.
* Perfect Binary Tree: A Binary tree is Perfect Binary Tree in which all internal nodes have two children and all leaves are at same level

6. AVL Trees
AVL tree is a self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtrees cannot be more than one for all nodes. 

7. Red-Black Trees
A red-black tree is a kind of self-balancing binary search tree where each node has an extra bit, and that bit is often interpreted as the colour (red or black). These colours are used to ensure that the tree remains balanced during insertions and deletions



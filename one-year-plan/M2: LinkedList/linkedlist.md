### 1. What's a Linked List?
A linked list organizes items sequentially, with each item storing a pointer to the next one. An item in a linked list is called a node. The first node is called the head. The last node is called the tail.

### 2. How many types of Linked List are there?
Singly, Doubly and Circular Linked Lists. 
- Singly linked list is a type of linked list in which each node is connected linearly to the next node.
- Doubly linked List is a type of linked list in which each node apart from storing its data has two links.
- Circular linked list: Think of singly linked list, except now the last node is connected to the first node as well.

### 3. When do we even use Linked List?
Linked lists are preferable over arrays when:

1. You need constant-time insertions/deletions from the list (such as in real-time computing where time predictability is absolutely critical)
2. You don't know how many items will be in the list. With arrays, you may need to re-declare and copy memory if the array grows too big
3. You don't need random access to any elements
4. You want to be able to insert items in the middle of the list (such as a priority queue)

It is actually used in stacks and queues as well!

### 4. Okay, what's the Python syntax?
1. First step is to create a class for the LinkedList:

class LinkedList:\
    def __init__(self):\
        self.head = None
        
        
2. Next, create another class to represent each node of the linked list:
class Node:\
    def __init__(self, data):\
        self.data = data\
        self.next = None\

For the full syntax refer to the py file

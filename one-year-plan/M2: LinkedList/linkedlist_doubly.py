# 1. Define a node class for a doubly-linked list (Hint: it should have a Node previous, next and int data)
# Note: singly linked list only has net and int data, no previous node


class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.previous = None


# 2. Define a Linked List class which will create an empty list with head and tail set to null.
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # return the string that will print the linked list
    def __repr__(self):
        string = ""
        if self.head == None:
            string += "Doubly Linked List Empty"
            return string

        string += f"Doubly Linked List:\n{self.head.data}"
        start = self.head.next
        while (start != None):
            string += f" -> {start.data}"
            start = start.next
        return string

    def append(self, data):
        # check if the list is empty, if so then the head and tail can point to the new node
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.count += 1
            return

        # Make the last node’s next point to the new node, then make the new node’s previous point to the last node,
        # and finally, make the tail point to the new node.
        self.tail.next = Node(data)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        self.count += 1

    # 3. Define an insert_to_start(int element), insert_to_end(int element) method.
    def insert_to_start(self, data):
        # Inserting at the front, make the first node’s previous point to the new node, then make the new node’s next point
        # to the first node, and finally, we make the head point to the new node.
        self.head.previous = Node(data)
        self.head.previous.next = self.head
        self.head = self.head.previous
        self.count += 1
        return

    def insert_to_end(self, data):
        # This is for inserting at the end of the Linked List, we could just simply append it
        self.append(data)
        return

    # 4. Define insert_at_position(int p, int element) method, which will insert the element at position p, and if p
    # is larger than the length of Linked List, it adds the element to the end.
    # at a specified index,

    # 1. Make the node's 'previous' point to the new node, so we use start.previous.next
    # 2. Make the node's 'previous' point to the node before the position
    # 3. Make the node's 'next' point to 'start' which was the node previously at that location
    # 4. Make the node (that was previously at that location)'s 'previous' point to the new node
    def insert_at_position(self, data, index):
        if (index > self.count):
            self.append(data)
            return
        start = self.head
        for _ in range(index):
            start = start.next
        start.previous.next = Node(data)
        start.previous.next.previous = start.previous
        start.previous.next.next = start
        start.previous = start.previous.next
        self.count += 1
        return

    # 5. Define insert_after_element(int target, int element) that will search for the first instance of target and
    # add the element after it. Similarly, define an insert_before_element(int target, int element). Both throw an
    # error if the element doesn’t exist.
    def insert_before_element(self, target, data):
        current = self.head
        while current != None:
            if current.data == target:      # data found
                current.previous.next = Node(data)
                current.previous.next.previous = current.previous
                current.previous.next.next = current
                current.previous = current.previous.next
                self.count += 1
                return
            current = current.next
        raise KeyError("Target does not exist in LL")  # Data Not found

    def insert_after_element(self, target, data):
        current = self.head
        while current != None:
            if current.data == target:      # data found
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                new_node.previous = current
                if new_node.next is not None:
                    new_node.next.previous = new_node
                self.count += 1
                return
            current = current.next
        raise KeyError("Target does not exist in LL")  # Data Not found

    # 6. Define print_list() that prints all elements, size() returns length of the list, and reverse() that reverses
    # the current list.
    def print_list(self):
        string = ""
        string += f"Doubly Linked List:  {self.head.data}"
        start = self.head.next
        while (start != None):
            string += f" -> {start.data}"
            start = start.next
        return string

    def size(self):
        return f"The length of the Linked List is:  {self.count}"

    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # 7. Define remove_element(int element) which deletes the first instance of the element (be careful if the
    # element removed is at head or tail position).
    def remove_element(self, data):
        def index(data):
            start = self.head
            for i in range(self.count):
                if (start.data == data):
                    return i
                start = start.next
            return KeyError("Target does not exist in LL")

        target_indice = index(data)
        # print(f"The index is: {target_indice}  {self.count - 1}")

        if target_indice == 0:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1
            return

        if target_indice == (self.count - 1):
            temp = self.head
            # Keep iterating until we get the second last element
            while (temp.next.next != None):
                temp = temp.next
            # Second last element is reached, set its 'next' to None
            temp.next = None
            self.count -= 1
            return

        start = self.head
        for i in range(target_indice - 1):
            start = start.next
        # start.previous.next, start.next.previous = start.next, start.previous
        next = start.next.next
        start.next = None
        start.next = next
        self.count -= 1
        return

    # Lastly, define remove_duplicates() that’ll remove any repeating elements. For example,
    # if your list is (2->3->22->4->2->3->5), it becomes (2->3->22->4->5).
    def remove_duplicate(self):
        distinct_list = []
        start = self.head
        for i in range(0, self.count):
            if start.data in distinct_list:
                self.remove_element(start.data)
            else:
                distinct_list.append(start.data)

            start = start.next
        return


nums = DLL()
nums.append('a'); nums.append('b'); nums.append('c'); nums.append('d'); nums.append('e')
nums.append('a'); nums.append('b'); nums.append('z'); nums.append('f');
nums.insert_to_start('g')
nums.insert_to_end('f'); nums.insert_to_end('f')
nums.remove_element('d')
nums
nums.remove_duplicate()
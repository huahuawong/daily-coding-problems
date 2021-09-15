# Small Project Ideas

# 1. Design a Queue using 2 stacks.
# Python program for implementation of stack

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def check_empty(self):
        return len(self.s1) == 0 and len(self.s2) == 0

    # Here we are pushing evrything into s1
    def enqueue(self, x):
        print(x + " pushed to queue")
        self.s1.append(x)

    # Now for the dequeue process, we are moving everything from s1 to s2, and then we return the first element on top
    # of the stack
    def dequeue(self):
        # if both s1 and s2 are zero, we should return error
        if len(self.s1) == 0 and len(self.s2) == 0:
            return "There is nothing in queue"
        # if s2 is empty and s1 has elements, that means we can 'dump' everything from s1 to s2
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1) != 0:
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop() + " popped from queue"
            # return self.s2.pop()
        else:       # this means s2 still has some elements so we'd just have to return the top of the stack using pop
            return self.s2.pop() + " popped from queue"


# Driver program to test above functions
q = Queue()
q.enqueue(str(10))
q.enqueue(str(20))
q.enqueue(str(30))
q.dequeue()
q.dequeue()
q.enqueue(str(40))
q.enqueue(str(50))
q.dequeue()
q.dequeue()
q.check_empty()


# 2. Implement 2 stacks in a single array.
class two_stacks:
    def __init__(self):
        self.s1 = []
        self.count1 = 0
        self.count2 = 0

    def enqueue_first(self, x):
        self.s1.append(x)
        self.count1 += 1

    def enqueue_second(self, x):
        if self.count2 == 0:
            self.s1.insert(len(self.s1), x)
            self.count2 += 1
            return
        self.s1.insert(len(self.s1) - self.count2, x)
        self.count2 += 1

    def dequeue_first(self):
        if self.count1 == 0:
            return "First stack is now empty"
        temp = self.s1.pop(self.count1 - 1)
        self.count1 -= 1
        return str(temp) + " popped from first stack"

    def dequeue_second(self):
        if self.count2 == 0:
            return "Second stack is now empty"
        temp = self.s1.pop(len(self.s1) - self.count2)
        self.count2 -= 1
        return str(temp) + " popped from second stack"


q2 = two_stacks()
q2.enqueue_first(1)
q2.enqueue_first(2)
q2.enqueue_first(3)
q2.enqueue_second(4)
q2.enqueue_second(5)
q2.enqueue_second(6)
q2.dequeue_second()
q2.dequeue_first()


# 3. Implement 3 stacks in a single array.
class KStacks:
    def __init__(self, k, n):
        self.k = k  # Number of stacks.
        self.n = n  # Total size of array holding
        # all the 'k' stacks.

        # Array which holds 'k' stacks.
        self.arr = [0] * self.n

        # All stacks are empty to begin with, (-1 denotes stack is empty).
        self.top = [-1] * self.k

        # Top of the free stack.
        self.free = 0

        # Points to the next element in either
        # 1. One of the 'k' stacks or,
        # 2. The 'free' stack.
        self.next = [i + 1 for i in range(self.n)]
        self.next[self.n - 1] = -1

    # Check whether given stack is empty.
    def isEmpty(self, sn):
        return self.top[sn] == -1

    # Check whether there is space left for
    # pushing new elements or not.
    def isFull(self):
        return self.free == -1

    # Push 'item' onto given stack number 'sn'.
    def push(self, item, sn):
        if self.isFull():
            print("Stack Overflow")
            return

        # Get the first free position to insert at.
        insert_at = self.free

        # Adjust the free position.
        self.free = self.next[self.free]

        # Insert the item at the free position we obtained above.
        self.arr[insert_at] = item

        # Adjust next to point to the old top of stack element.
        self.next[insert_at] = self.top[sn]

        # Set the new top of the stack.
        self.top[sn] = insert_at

    # Pop item from given stack number 'sn'.
    def pop(self, sn):
        if self.isEmpty(sn):
            return None

        # Get the item at the top of the stack.
        top_of_stack = self.top[sn]

        # Set new top of stack.
        self.top[sn] = self.next[self.top[sn]]

        # Push the old top_of_stack to the 'free' stack.
        self.next[top_of_stack] = self.free
        self.free = top_of_stack

        return self.arr[top_of_stack]

    def printstack(self, sn):
        top_index = self.top[sn]
        while (top_index != -1):
            print(self.arr[top_index])
            top_index = self.next[top_index]


# Driver Code
if __name__ == "__main__":
    # Create 3 stacks using an
    # array of size 10.
    kstacks = KStacks(3, 10)

    # Push some items onto stack number 2.
    kstacks.push(15, 2)
    kstacks.push(45, 2)

    # Push some items onto stack number 1.
    kstacks.push(17, 1)
    kstacks.push(49, 1)
    kstacks.push(39, 1)

    # Push some items onto stack number 0.
    kstacks.push(11, 0)
    kstacks.push(9, 0)
    kstacks.push(7, 0)

    print("Popped element from stack 2 is " +
          str(kstacks.pop(2)))
    print("Popped element from stack 1 is " +
          str(kstacks.pop(1)))
    print("Popped element from stack 0 is " +
          str(kstacks.pop(0)))

    kstacks.printstack(0)

# This code is contributed by Varun Patil

# 4. Design a stack with the following methods: Push, pop, peek, get_min, get_max. All of them should be O(1).


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


# 4. Design a stack with the following methods: Push, pop, peek, get_min, get_max. All of them should be O(1).


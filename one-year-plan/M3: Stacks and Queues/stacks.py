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
class Queue:
    def __init__(self):
        self.s1 = []

    def enqueue_first(self, x):
        self.s1.append(x)

    def enqueue_second(self, x):
        self.s1.append(x)


arr = []
arr.append(2)
arr.append(2)
arr.insert(8, 5)
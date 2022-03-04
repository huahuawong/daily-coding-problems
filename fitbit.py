# Q1
# Given a linked list, rearrange the node values such that they appear in alternating low -> high -> low -> high ... form. 
# For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4.

# THe idea is to start with the first and second node. If the first node (prev) is bigger than the second node (current), then we swap the values since
# we are starting with low-> high -> low -> ....
# Similarly, if the next of current and second next of current is bigger than current, that'd mean that we have a window of 3 increasing numbers, for instance, 3, 4, 5,
# so to set this right, we have to swap the 3 with 4

# A linked list node
class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


# Utility Function
# Function to print given linked list
def printList(head):

	ptr = head
	while ptr:
		print(ptr.data, end=" -> ")
		ptr = ptr.next

	print("None")


# Rearrange the linked list so that it has alternating high, low values
def rearrange(head):

	# empty list
	if head is None:
		return None

	prev = head
	curr = head.next

	# start from second node
	while curr:

		# If the prev node is greater than current node, swap their values
		if prev.data > curr.data:
			temp = prev.data
			prev.data = curr.data
			curr.data = temp

		# if next node is greater than current node, swap their values
		if curr.next and curr.next.data > curr.data:
			temp = curr.next.data
			curr.next.data = curr.data
			curr.data = temp

		# update prev and curr node
		prev = curr.next

		if curr.next is None:
			break

		curr = curr.next.next

	return head
	
# Rearrange the linked list so that it has alternating high, low values
if __name__ == '__main__':

	# input keys
	keys = [1, 2, 3, 4, 5, 6, 7, 8, 6]

	head = None
	for i in reversed(range(len(keys))):
		head = Node(keys[i], head)

	head = rearrange(head)
	printList(head)

	
# Q2 Write a Python Program to Check Common Letters in Two Input Strings?
s1 = ("Hello world")
s2 = ("Hey")

common_letters = list((set(s1) & set(s2)))

for letter in common_letters:
    print(letter)


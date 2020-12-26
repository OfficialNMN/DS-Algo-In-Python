from collections import deque

class Stack:
	def __init__(self):
		self.container=deque()

	def traverse(self):
		return self.container

	def push(self,value):
		self.container.append(value)

	def pop(self):
		self.container.pop()

	def peek(self):
		return self.container[-1]

	def isempty(self):
		return len(self.container)==0

	def size(self):
		return len(self.container)

s=Stack()
s.push(4)
s.push(3)
s.push(5)
s.push(6)
print(s.traverse())
s.pop()
print(s.peek())
print(s.size())

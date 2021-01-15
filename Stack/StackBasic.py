'''Stack using Array'''

class Stack:
	def __init__(self,maxsize):
		self.maxsize=maxsize
		self.container=[]

	def traverse(self):
		for i in reversed(self.container):
			print(i,end='\n')

	def push(self,value):
		if self.size()==self.maxsize:
			return 'OverflowError'
		else:
			self.container.append(value)

	def pop(self):
		if self.isempty():
			return "UnderflowError"
		else:
			self.container.pop()

	def peek(self):
		return self.container[-1]

	def isempty(self):
		return len(self.container)==0

	def size(self):
		return len(self.container)

s=Stack(3)
print(s.pop())
s.push(4)
s.push(3)
s.push(5)
print(s.push(6))
print('---')
s.traverse()
print('---')
s.pop()
print('Peeked '+str(s.peek()))
print('Size is '+str(s.size()))

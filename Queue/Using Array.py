''' Queue using Array '''

class Queue:
	def __init__(self,maxsize):
		self.queue=[]
		self.maxsize=maxsize

	def enqueue(self,value):
		if self.size()==self.maxsize:
			print('OverflowError')
		else:
			self.queue.append(value)

	def dequeue(self):
		if self.isEmpty():
			print('UnderflowError')
		else:
			self.queue.pop(0)

	def traverse(self):
		return self.queue

	def size(self):
		return len(self.queue)

	def peek(self):
		return self.queue[0]

	def isEmpty(self):
		return len(self.queue)==0


q=Queue(10)
print(q.isEmpty())
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.dequeue()
print(q.peek())
print(q.traverse())
q.dequeue()

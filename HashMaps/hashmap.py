'''TimeComplexity of Searching/Addition/Deletion----O(1)'''

class HashTable:
	def __init__(self):
		self.max=100
		self.arr=[None for i in range(self.max)]

	def gethash(self,key):
		h=0
		for char in key:
			h+=ord(char)
		return h%100

	def __getitem__(self,index):
		h=self.gethash(index)
		return self.arr[h]

	def __setitem__(self,key,value):
		h=self.gethash(key)
		self.arr[h]=value

	def __delitem__(self,key):
		h=self.gethash(key)
		self.arr[h]=None

t=HashTable()
t['march 6']=310
t['march 7']=311
t['march 8']=312
t['march 9']=313
t['march 5']=314

del t['march 5']

print(t['march 6'])

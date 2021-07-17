# Partitioning the individuals into different sets according to the groups in which 
# they fall. This method is known as disjoint set data structure which maintains 
# collection of disjoint sets and each set is represented by its representative which
#  is one of its members.

# Union: It takes, as input, two elements. And finds the representatives of their 
# sets using the find operation, and finally puts either one of the trees 
# (representing the set) under the root node of the other tree, effectively merging 
# the trees and the sets

# Find: To find whether x and y belong to same group or not, i.e., 
# to find if x and y are direct/indirect friends

class DisjointSet:
	def __init__(self,vertices):
		self.vertices=vertices
		self.parent={}
		for v in vertices:
			self.parent[v]=v
		self.rank=dict.fromkeys(vertices,0)

	# time complexity - O(1)
	def find(self,item):
		if item==self.parent[item]:
			return item
		return self.find(self.parent[item])

	# Implemented Union by Rank ---> time complexity - O(1)
	def union(self,x,y):
		xroot=self.find(x)
		yroot=self.find(y)
		if self.rank[xroot]<self.rank[yroot]:
			self.parent[xroot]=yroot
		elif self.rank[xroot]>self.rank[yroot]:
			self.parent[yroot]=xroot
		else:
			self.parent[yroot]=xroot
			self.rank[xroot]+=1

vertices=['A','B','C','D','E']
ds=DisjointSet(vertices)
ds.union('A','B')
print(ds.find('B'))


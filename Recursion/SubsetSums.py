# to return sum of all subsets that can be formed using elements of given array

class Solution:
	def subsetSums(self, arr, N):
	    sets=[]
	    self.subset(arr,N,0,0,sets)
	   # to return sorted answer
	    sets.sort()
	    return sets
	
	def subset(self,arr,N,ind,summ,sets):
	   # if ind reaches the end of arr we stop recursion
	    if ind==N:
	        sets.append(summ)
	        return 
	   # when element is chosen in sum
	    self.subset(arr,N,ind+1,summ+arr[ind],sets)
       # when element is not chosen in sum  
	    self.subset(arr,N,ind+1,summ,sets)
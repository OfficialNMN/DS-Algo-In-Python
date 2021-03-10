# Using recursion to shift (n-1) elements to other stack and then shift them back and at last pushing the last element(nth) to the original stack 

def reverse(s1,s2):
	if len(s1)<=1:
		return 
	while(len(s1)!=1):
		s2.append(s1.pop())
	last=s1.pop()
	while(len(s2)!=0):
		s1.append(s2.pop())
	reverse(s1,s2)
	s1.append(last)

s1=[1,2,3,4]
reverse(s1,[])
print(s1)

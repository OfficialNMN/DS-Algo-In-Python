# longest consecutive subsequence
def lcs(A):
	dic={}
	# making every key as True making every element as starting of sequence
	for i in A:
		dic[i]=True
	# if previous value is already present as key then making that key false as it will not be starting of the sequence
	for i in A:
		if i-1 in dic:
			dic[i]=False
	# initisalizing maxlength=0
	maxl=0
	for i in A:
		if dic[i]==True:
			# temp means the default length for each sequence 
			temp=1
			# iterate till (i+temp) is there in dictionary
			while ((i+temp) in dic.keys()):
				temp+=1
			# replace maxlength if temp is greater
			if temp>maxl:
				maxl=temp
	return maxl

		
print(lcs([ 6, 4, 5, 2, 3]))
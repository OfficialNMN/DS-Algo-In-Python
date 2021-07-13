# To print a number in words eg: 2048--> Two Zero Four Eight

def numtoword(n):
	spellings={0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
	if n==0:
		return
	numtoword(n//10)
	print(spellings[n%10],end=' ')	

numtoword(5096)
# 1. To check anagram

def anagram(str1,str2):
	if len(str1)!= len(str2):
		return False
	else:
		if sorted(str1)!=sorted(str2):
			return False
		return True
print(anagram('geeks','eeksg'))

# Panagram string - all 26 alphabets are present in the string


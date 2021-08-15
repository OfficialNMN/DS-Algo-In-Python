def longestSubstr(s):
	# map to store previous occurences of chars 
	hashmap={}
	length=0
	start=0

	for end in range(len(s)):
		if s[end] in hashmap:
			# store the last occurence of current element
			start=max(start,hashmap[s[end]]+1)
		hashmap[s[end]]=end
		length=max(length,end-start+1)
	return length

print(longestSubstr('abcabcbb'))
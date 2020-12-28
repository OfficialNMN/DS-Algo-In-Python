def balanced(expr):
	stack=[]
	for i in expr:
		if i in ['[','{','(']:
			stack.append(i)
		else:
			if len(stack)==0:
				return False
			char=stack.pop()
			if char=='(':
				if i!=')':
					return False
			elif char=='{':
				if i!='}':
					return False
			elif char=='[':
				if i!=']':
					return False
	if len(stack)==0:
		return True
	return False

print(balanced('{()}['))

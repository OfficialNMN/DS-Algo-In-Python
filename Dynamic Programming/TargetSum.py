# Count the number of subsets with given difference d in arr
'''
let s1 and s2 be the sum of 2 subsets
s1 + s2 = sum(arr)
s1 - s2 = d
=> s1 = (d + sum(arr))/2

Therefore the problem turn into calculating the number of subsets with given sum s1
'''

# Target Sum is a variation of the above problem
# here s1 - s2 can be converted to s1 + (-s2) = taregt_sum 
# and then can be solved as above problem
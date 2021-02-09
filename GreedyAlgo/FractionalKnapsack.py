# Fractional Knapsack Problem----> A thief has to steal items with maximum worth within a limit of certain weight(kg) in the bag.

class Item:
	def __init__(self,weight,value):
		self.weight = weight
		self.value = value
		self.ratio = value/weight

def knapsack(items,capacity):
	items.sort(key=lambda x : x.ratio,reverse=True)
	usedcapacity=0
	profit=0
	for i in items:
		if usedcapacity + i.weight <= capacity:
			usedcapacity += i.weight
			profit += i.value
		else:
			unusedweight = capacity - usedcapacity
			value = i.ratio * unusedweight
			usedcapacity += unusedweight
			profit += value
		if usedcapacity==capacity:
			break
	print(profit)

item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10,60)
cList = [item1, item2, item3]

knapsack(cList, 50)

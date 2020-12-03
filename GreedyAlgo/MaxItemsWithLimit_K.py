# You have to buy maximum items that can be purchased with in a given cost limit k.

def items(cost,k):
    item=0
    cost.sort()              
    for i in cost:
        if i<k:
            k=k-i
            item+=1
    return item

#1.Knapsack Problem----> A thief enters a house to steal items with maximum worth within a limit of k items only in the bag.

def items(cost,k):
    cost.sort()
    cost.reverse()             # reversed the sorted array to get k largest items
    return sum(cost[:k])

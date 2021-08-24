def Mincoins(V):
    coins = [1, 2, 5, 10, 20, 50,
            100, 500, 1000]
    n = len(coins)
    ans = []
    i = n - 1
    while(i >= 0):

        while (V >= coins[i]):
            V -= coins[i]
            ans.append(coins[i])
 
        i -= 1
    return ans
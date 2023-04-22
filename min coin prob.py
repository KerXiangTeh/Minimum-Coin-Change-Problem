
# Greedy approach: suboptimal solution
def greedyChange(n):
    coins = [25, 20, 10, 5, 1]
    minCoins = 0

    for coin in coins:
        minCoins += n // coin
        n %= coin
    
    return minCoins

# Optimal solution: considers every coin denominations
def optimalChange(n):
    coins = [1, 5, 10, 20, 25]
    sol = [float('inf')] * (n + 1)
    sol[0] = 0

    for i in range(1, n + 1):
        for coin in coins:
            if i - coin >= 0:
                sol[i] = min(sol[i], sol[i - coin] + 1)
    return sol[n]
    
# Testing algorithms
n = 40
greedy = greedyChange(n)
optimal = optimalChange(n)

print(f"Greedy solution for {n} change: {greedy}")
# Greedy solution for 40 change: 3

print(f"Optimal solution for {n} change: {optimal}")
# Optimal solution for 40 change: 2
def find_combinations(n, coins, index=0, combination=None):
    if combination is None:
        combination = []
    
    if n == 0:
        print(", ".join(f"{coin}×{count}" for coin, count in combination))  
        return
    
    if index >= len(coins):
        return  
    
    for i in range(n // coins[index] + 1):
        combination.append((coins[index], i))  
        find_combinations(n - i * coins[index], coins, index + 1, combination)
        combination.pop()  


coins = [500, 200, 100, 50 ,10,1]
n = int(input("Enter the amount of money: "))

print(f"Possible ways to split {n}:")
find_combinations(n, coins)





# I took some help from google and youtube.  :)
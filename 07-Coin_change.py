def countRecur(coins, n, sum, memo):
  
   
    if sum == 0:
        return 1

    if sum < 0 or n == 0:
        return 0

   
    if memo[n - 1][sum] != -1:
        return memo[n - 1][sum]

    
    memo[n - 1][sum] = (countRecur(coins, n, sum - coins[n - 1], memo) + 
                        countRecur(coins, n - 1, sum, memo))
    return memo[n - 1][sum]

def count(coins, sum):
    memo = [[-1 for _ in range(sum + 1)] for _ in range(len(coins))]
    return countRecur(coins, len(coins), sum, memo)

if __name__ == "__main__":
    coins = [1, 2, 3]
    sum = 5
    print(count(coins, sum))
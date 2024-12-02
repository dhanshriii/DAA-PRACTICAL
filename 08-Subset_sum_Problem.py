def isSubsetsum(arr, sum):
    n = len(arr)


    dp = [[False] * (sum + 1) for _ in range(n + 1)]


    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < arr[i - 1]:
              
                
                dp[i][j] = dp[i - 1][j]
            else:
              
               
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    return dp[n][sum]


arr = [3, 34, 4, 12, 5, 2]
sum_value = 9

if isSubsetsum(arr, sum_value):
    print("True")
else:
    print("False")
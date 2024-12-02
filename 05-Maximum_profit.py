def maxProfit(prices, n):
 
    profit = 0
    currentDay = n - 1
 
    # Start from the last day
    while (currentDay > 0):
        day = currentDay - 1
 
       
        while (day >= 0 and
              (prices[currentDay] >
               prices[day])):
            profit += (prices[currentDay] -
                       prices[day])
                        
            day -= 1
         
    
        currentDay = day;
     

    return profit;
 

prices = [ 2, 3, 5 ]
 
N = len(prices)
 

print(maxProfit(prices, N))
 
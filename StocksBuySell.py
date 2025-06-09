def calculateProfit(arr,arr_size):
    profit = 0
    for i in range (1,arr_size):
        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]
    return profit
prices = [625,874,347,248,901,1503,2001]
profit = calculateProfit(prices,len(prices))
print("Maximum Price is :-",profit)
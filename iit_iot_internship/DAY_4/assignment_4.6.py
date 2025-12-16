prices = [105, 110, 108, 112, 115, 116, 114]

i = 0
while i <= len(prices) - 3:  #Loop runs while i is 0, 1, 2, 3, 4 and prevents index out of range error
    avg = (prices[i] + prices[i+1] + prices[i+2]) / 3
print("3 days average:", round(avg, 2)) #round(avg, 2) limits the result to 2 decimal places
i+=1
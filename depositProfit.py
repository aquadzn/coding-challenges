def depositProfit(deposit, rate, threshold):
    i = 0
    while deposit < threshold:
        deposit += deposit * rate * .01
        i+=1
    return i
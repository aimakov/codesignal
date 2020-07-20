## code for finding amount of year till balance is over threshold

def depositProfit(deposit, rate, threshold):
    ans = 0
    while deposit < threshold:
        deposit*=rate/100+1
        ans+=1
    return ans
        
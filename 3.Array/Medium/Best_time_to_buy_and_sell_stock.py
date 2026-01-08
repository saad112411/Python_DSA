"""
Given an array arr of n integers, where arr[i] represents price of the stock on the ith day.
Determine the maximum profit achievable by buying and selling the stock at most once. 
The stock should be purchased before selling it, and both actions cannot occur on the same day.

Input: arr = [10, 7, 5, 8, 11, 9, 1, 2]
Output: 6
Explanation: Buy on day 3 (price = 5) and sell on day 5 (price = 11), profit = 11 - 5 = 6.

Input: arr = [5, 4, 3, 2, 1]
Output: 0
Explanation: In this case, no transactions are made. Therefore, the maximum profit remains 0.
"""

def get_max_profit(arr):
    if not arr or len(arr) < 2:
        return 0
    min_price = arr[0]
    max_profit = 0
    for i in range(1, len(arr)):
        current_price = arr[i]
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)
    return max_profit
     

arr=[10, 7, 5, 8, 11, 9]
#print(get_max_profit(arr))


def get_a_max_profit(arr):
    min_price=arr[0]
    max_profit=0
    for i in range(1,len(arr)):
        current_price=arr[i]
        potential_profit=current_price-min_price
        max_profit=max(max_profit,potential_profit)
        min_price=min(min_price,current_price)
    return max_profit

arr=[10, 7, 5, 8, 11, 9]
print(get_a_max_profit(arr))
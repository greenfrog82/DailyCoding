# Problem

Input array에서, index는 해당 날짜를, value는 그 날의 주가를 뜻합니다.
최대 1회의 거래 (1 거래= 1주를 매수하고 매도하는 거래)를 통하여 얻을 수 있는 최대수익을 구현하는 algorithm을 구현하시오. 매수 전에 매도 할 수 없습니다.


You have an array for which the ith element is the price of a given stock on day i.

You can only make up to 1 transaction (transaction = buy one and sell one share). You cannot sell a stock before you buy.

Design an algorithm to find the maximum profit.


[Example 1]
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

[Example 2]
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


    
    
  
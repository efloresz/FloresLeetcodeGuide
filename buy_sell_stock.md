``` Best Time to Buy and Sell Stock```

<img width="754" alt="Screenshot 2023-11-22 at 11 06 00 AM" src="https://github.com/efloresz/FloresLeetcodeGuide/assets/110843762/74cefd2c-f9cd-4a63-bf7f-2e5fb44ccb3b">

```python
Solution:
# intution approach:
# [3, 1, 5, 7, 2, 6] prices array
# sliding window approach we compare 1 value to rest of vals
# buy day 1 for $3 -> sell day 2 for $1 = -2 profit
# buy day 1 for $3 -> sell day 3 for $5 = +2 profit
# additional approach binary search:
# pick a day to buy & eliminate vals to left
# iterate array for all values to find max profit

# refined approach:
# compare min and max (Two pointers L (buy) = day 1; R (sell) = day 2)
# keep lowest value in left pointer (buy) and shift right (sell)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProf = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProf = max(maxProf, profit)
            else:
                left = right
            right += 1   
        return maxProf         
                
```

```python
# Difficulty: Easy

# Data Structures Used: Sliding Window & Two Pointers

# Time Complexity: O(n)

# Space Complexity: O(1)

```

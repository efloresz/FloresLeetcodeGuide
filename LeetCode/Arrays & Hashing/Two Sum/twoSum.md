```Two Sum ```

<img width="679" alt="Screenshot 2023-11-17 at 8 37 41 PM" src="https://github.com/efloresz/FloresLeetcodeGuide/assets/110843762/01418d93-25b2-4f45-8492-126869db4cd3">

```python
Solution
# Create a hash map of every value in input array
# mapping -> value : index
# target - value in array -> search for value in map
# map is intially empty and you iterate through array once

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        startingMap = {} # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in startingMap:
                return [startingMap[diff], i]
            startingMap[n] = i
        return               

```

```python
# Difficulty: Easy

# Data Structures Used: Arrays & Hashing

# Time Complexity: O(n)

# Space Complexity: O(n)

```
